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
import sys

import click
import toml

from aomie import __version__
from aomie.handling import (download_files, extract_files, insert_files,
                            fetch_files)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--version', is_flag=True, default=False,
              help='Display version.')
def cli(ctx, version):
    """aomie: OMIE electricity market data handling tool"""
    if ctx.invoked_subcommand is None and not version:
        click.echo(ctx.get_help())
    if version:
        click.echo(__version__)


@cli.command(short_help='Download OMIE data.')
@click.argument('config')
@click.option('--extract', '-e', is_flag=True, default=False,
              help='Extract downloaded files.')
def download(config, extract):
    """Download OMIE files to local destination."""
    cfg = toml.load(config)
    download_files(**cfg)
    if extract:
        extract_files(**cfg)


@cli.command(short_help='Extract data from zip files.')
@click.argument('config')
def extract(config):
    """Extract zip files."""
    cfg = toml.load(config)
    extract_files(**cfg)


@cli.command(short_help='Insert data into SQLite database.')
@click.argument('config')
def insert(config):
    """Insert data into SQLite database."""
    cfg = toml.load(config)
    insert_files(**cfg)


@cli.command(short_help='Download, extract and insert files into database.')
@click.argument('config')
def fetch(config):
    """Download, extract and insert into database."""
    cfg = toml.load(config)
    fetch_files(**cfg)
