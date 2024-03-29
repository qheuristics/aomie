#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='aomie',
    version='0.0.0',
    license='MIT',
    description='Pure Python 3 open source library to handle Iberian electricity market data published by OMIE.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    long_description_content_type='text/x-rst',
    author='Guillermo Lozano Branger',
    author_email='qheuristics@gmail.com',
    url='https://github.com/qheuristics/aomie',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    project_urls={
        'Documentation': 'https://aomie.readthedocs.io/',
        'Changelog': 'https://aomie.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/qheuristics/aomie/issues',
    },
    keywords=[
        'OMIE', 'electricity market', 'data handling',
    ],
    python_requires='>=3.6',
    install_requires=[
        'click',
        'toml',
        'pandas',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'wheel',
    ],
    entry_points={
        'console_scripts': [
            'omie = aomie.cli:cli',
            'om = aomie.cli:cli',
        ]
    },
)
