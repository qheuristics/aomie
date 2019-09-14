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
containing text files of daily data with different levels of aggregation (e.g. by bidding unit or technology).
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
