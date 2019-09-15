========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/aomie/badge/?style=flat
    :target: https://readthedocs.org/projects/aomie
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/qheuristics/aomie.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/qheuristics/aomie

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/qheuristics/aomie?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/qheuristics/aomie

.. |requires| image:: https://requires.io/github/qheuristics/aomie/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/qheuristics/aomie/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/qheuristics/aomie/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/qheuristics/aomie

.. |version| image:: https://img.shields.io/pypi/v/aomie.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/aomie

.. |commits-since| image:: https://img.shields.io/github/commits-since/qheuristics/aomie/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/qheuristics/aomie/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/aomie.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/aomie

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/aomie.svg
    :alt: Supported versions
    :target: https://pypi.org/project/aomie

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/aomie.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/aomie


.. end-badges

aomie is a Python 3 open source library that helps you handle Iberian electricity market data published by OMIE.

Over 80 statistical indicators of historical data of the Iberian electricity market are published at
http://www.omie.es/aplicaciones/datosftp/datosftp.jsp. These indicators are available as downloadable zip files
containing text files of daily data with different levels of aggregation (by bidding unit, technology, etc.).
To analyse these indicators over time or to make comparison between them you need to follow these steps:

- Download all the data files covering the time horizon of interest
- Extract the daily text files from the downloaded zip files
- Combine the content of potentially thousands of files

aomie automates this workflow. It  downloads all files of the required metric over a user-specified
time period, unzips the downloaded files and inserts their content into a SQLite database. Once in the database,
data analysis can be conveniently performed using SQLite directly or with tools such as pandas in Python or
dplyr in R.

* Free software: MIT license

Installation
============

::

    pip install aomie

Usage
=====

Import the aomie library into your Python libraries, scripts or applications as usual::

    import aomie

amoie includes a succint command line interface that make OMIE data handling extremely easy.

From the command line help:

.. raw:: html

        <div>
        <PRE>
        <B>AOMIE</B>                         User Commands                        <B>AOMIE</B>

        Usage: omie [OPTIONS] COMMAND [ARGS]...

          aomie: OMIE electricity market data handling tool

        Options:
          --version               Display version.
          -f, --config-file TEXT  Configuration file name and location.
          -d, --display-config    Display configuration
          -c, --config KEY VALUE  Overrides a config key/value pair.
          -v, --verbose           Enables verbose mode.
          --help                  Show this message and exit.

        Commands:
          download  Download OMIE data.
          extract   Extract data from zip files.
          fetch     Download, extract and insert files into database.
          insert    Insert data into SQLite database.

        </PRE></div>


Some usage examples follow.

A typical aomie starts by jointly setting the required configuration parameters through
a toml configuration file

::

    omie -f myconfig.toml


The configuration settings included in myconfig.toml are now avalaible to omie commands
without having to explicitly call the toml config file again, e.g. to download data just type

::

    omie download

Obviously you can use a different config file at any time

::

    omie -f otherconfig.toml download

or just change some of the configuration settings

::

    omie -c end 200512

To check the current configuration settings type

::

    omie -d

This will return something like this

.. raw:: html

        <div>
        <PRE>
        &lt;Config OrderedDict([('servername', 'www.omel.es'),
                     ('fichero', 'pdbf'),
                     ('start', 200501),
                     ('end', 200512),
                     ('path', '_data3/'),
                     ('dbname', 'test2.db3'),
                     ('filter_unit',
                      ['BES5',
                       'CTN4',
                       'PGR5',
                       'ECT2'])])&gt;
        </PRE></div>

Once the zip files have been downloaded we can extract them like this

::

    omie extract

To complete the workflow by inserting the extracted data into a SQLite database type

::

    omie insert

The aomie commmand fetch bundles all the key data handling tasks. To run these
tasks in a single step just type

::

    omie -f myconfig.toml -c end 200512 fetch

Given the convenience of the fetch command, other commands that just perform one of
the steps in omie workflow may seem redundant. Note however that omie data
handling tasks covering long time horizons may involve downloading and processing
hundreds of MBs that are disk and time consuming, and you may therefore prefer to proceed
cautiously step by step.

More information can be found in the command line help, e.g. to learn more about
aomie commands such as download type

::

    omie download --help

to display this

.. raw:: html

        <div>
        <PRE>
        <B>AOMIE</B>                         User Commands                        <B>AOMIE</B>

        Usage: omie download [OPTIONS]

          Download OMIE files to local destination.

        Options:
          -e, --extract  Extract downloaded files.
          --help         Show this message and exit.

        </PRE></div>


From this help we learn that we can download and extract in a single step by typing

::

    omie download -e


Documentation
=============


https://aomie.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
