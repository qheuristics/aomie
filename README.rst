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

Python 3 open source library to handle Iberian electricity market data published by OMIE.

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

To run the all tests run::

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
