"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m aomie` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``aomie.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``aomie.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import os
import shutil
import sys
from collections import OrderedDict
from pprint import pformat

import click
import toml

from aomie import __version__
from aomie.handling import download_files
from aomie.handling import extract_files
from aomie.handling import fetch_files
from aomie.handling import insert_files

TML = '.omie\\omie.toml'

MSGNOCFG = ('No amoie configuration available.\n'
            'Type omie --help for information about '
            'amoie configuration.')


class Config(object):

    def __init__(self, source=None, path=None):
        self.verbose = False
        self.source = source
        if path:
            pth = os.path.abspath(path)
        else:
            pth = os.getcwd()
        tml = os.path.join(pth, TML)
        if source:
            click.echo(f'Reading configuration source from: \n\t{source}')
            src = os.path.abspath(source)
            os.makedirs(os.path.dirname(tml), exist_ok=True)
            shutil.copy(src, tml)
            self.home = tml
        try:
            self.config = toml.load(tml, _dict=OrderedDict)
        except FileNotFoundError:
            pass

    def set_config(self, key, value):
        self.config[key] = value
        tml = os.path.join(os.getcwd(), TML)
        with open(tml, 'w') as f:
            toml.dump(self.config, f)
            # f.write(pformat(self.config))
        if self.verbose:
            click.echo('Updating configuration:\n\tconfig[%s] = %s' %
                       (key, value), file=sys.stderr)

    def __repr__(self):
        try:
            return '<Config %s>' % pformat(self.config)
        except AttributeError:
            return '<Config %s>' % dict()


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, default=False,
              help='Display version.')
@click.option('--config-file', '-f', required=False,
              help='Configuration file name and location.')
@click.option('--display-config', '-d', is_flag=True, default=False,
              help='Display configuration')
@click.option('--config', '-c', nargs=2, multiple=True,
              metavar='KEY VALUE', help='Overrides a config key/value pair.')
@click.option('--verbose', '-v', is_flag=True,
              help='Enables verbose mode.')
@click.pass_context
def cli(ctx, config_file, config, verbose, version, display_config):
    """aomie: OMIE electricity market data handling tool"""
    """Create a config object to handle data handling specs."""
    # Remember the config object as the context object.  From
    # this point onwards other commands can refer to it by using the
    # @pass_config decorator.
    if version:
        click.echo(f'aomie {__version__}')
        return
    source = None
    if config_file:
        source = os.path.abspath(config_file)
    ctx.obj = Config(source)
    ctx.obj.verbose = verbose
    for key, value in config:
        ctx.obj.set_config(key, value)
    if display_config:
        print(ctx.obj)


@cli.command(short_help='Download OMIE data.')
@click.option('--extract', '-e', is_flag=True, default=False,
              help='Extract downloaded files.')
@pass_config
def download(config, extract):
    """Download OMIE files to local destination."""
    try:
        cfg = config.config
    except AttributeError:
        click.echo(MSGNOCFG)
        return
    pth = os.path.abspath(cfg['path'])
    click.echo(f'Downloading files to:\n\t{pth}')
    download_files(**cfg)
    if extract:
        extract_files(**cfg)


@cli.command(short_help='Extract data from zip files.')
@pass_config
def extract(config):
    """Extract zip files."""
    try:
        cfg = config.config
    except AttributeError:
        click.echo(MSGNOCFG)
        return
    pth = os.path.abspath(cfg['path'])
    click.echo(f'Extracting files at {pth}')
    extract_files(**cfg)


@cli.command(short_help='Insert data into SQLite database.')
@pass_config
def insert(config):
    """Insert data into SQLite database."""
    try:
        cfg = config.config
    except AttributeError:
        click.echo(MSGNOCFG)
        return
    pthfrom = os.path.abspath(cfg['path'])
    pthto = os.path.abspath(cfg['dbname'])
    click.echo(f'Inserting files from:\n\t {pthfrom}\nto:\n\t {pthto}')
    insert_files(**cfg)


@cli.command(short_help='Download, extract and insert files into database.')
@pass_config
def fetch(config):
    """Download, extract and insert into database."""
    try:
        cfg = config.config
    except AttributeError:
        click.echo(MSGNOCFG)
        return
    fetch_files(**cfg)
