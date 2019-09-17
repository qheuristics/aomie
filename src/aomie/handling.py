import glob
import os
import shutil
import sqlite3
import urllib.request
import zipfile
from functools import partial

import numpy as np
import pandas as pd

dtype = {'year': np.int32, 'month': np.int32, 'day': np.int32,
         'hour': np.int32, 'unit': str, 'energy': np.float64,
         'offer_type': np.int32}


def _move_files(source, destination):
    for tree, fol, fs in os.walk(source):
        for f in fs:
            try:
                shutil.move(tree + os.sep + f, os.path.join(destination, f))
            except shutil.Error:
                continue


_skip_read_csv = partial(pd.read_csv, sep=';', skipfooter=1, header=None,
                         index_col=False, engine='python',
                         names=['year', 'month', 'day', 'hour', 'unit',
                                'energy', 'offer_type'],
                         dtype=dtype)


def download_files(servername, fichero, path, start, end, **kwargs):
    fileroot = f'/datosPub/{fichero}/'
    os.makedirs(os.path.dirname(path), exist_ok=True)

    items = [*map('pdbf_{}.zip'.format,
                  pd.date_range(start=pd.to_datetime(str(start),
                                                     format='%Y%m'),
                                end=pd.to_datetime(str(end), format='%Y%m'),
                                freq='MS').strftime('%Y%m'))]
    for item in items:
        filename = fileroot + item
        localname = path + item
        remoteaddr = 'http://%s%s' % (servername, filename)
        print(remoteaddr)
        urllib.request.urlretrieve(remoteaddr, localname)

    print('\nDownloaded %s files to %s' % (str(len(items)), path[:-1]))


def extract_files(path, **kwargs):
    with os.scandir(path) as it:
        for entry in it:
            filename, file_extension = os.path.splitext(entry.name)
            if entry.is_file() and file_extension == '.zip':
                try:
                    with zipfile.ZipFile(entry, 'r') as zip_ref:
                        zip_ref.extractall(os.path.join(path, filename))
                except zipfile.BadZipFile:
                    print('Bad zip file', entry.name)


def gather_files(sources, destination, remove=False):
    """Move files in sources to destination."""
    os.makedirs(destination, exist_ok=True)
    for s in sources:
        _move_files(s, destination)
        if remove:
            # remove source folder
            shutil.rmtree(s)


def _pack_files(sources, filter_unit, **kwargs):
    dfs = []
    for f in sources:
        try:
            skiprows = 1
            d = _skip_read_csv(f, skiprows=skiprows)
        except ValueError:
            skiprows = 2
            d = _skip_read_csv(f, skiprows=skiprows)
        dfs.append(d)

    df = pd.concat(dfs, ignore_index=True)
    df = df[df.unit.isin(filter_unit)]
    return df


def insert_files(path, filter_unit, dbname, fichero, delatstart=True,
                 ifexists='append', display=True, **kwargs):
    sources = glob.glob(f'{os.path.join(path, fichero)}_*/')
    packs = [glob.glob(f'{s}*.*') for s in sources]
    dfs = map(partial(_pack_files, filter_unit=filter_unit), packs)

    with sqlite3.connect(dbname) as conn:
        if delatstart:
            conn.execute(f'DROP TABLE IF EXISTS {fichero};')
        for df in dfs:
            df.to_sql(fichero, conn, if_exists=ifexists, index=False)
        if display:
            print(pd.read_sql(f'select * from {fichero}', conn))


def fetch_files(path, fichero, filter_unit, dbname, servername, start, end,
                **kwargs):
    download_files(servername, fichero, path, start, end)
    extract_files(path)
    insert_files(path, filter_unit, dbname, fichero)
