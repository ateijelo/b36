#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

setup(
    name='ateijelo.b36',
    version='0.1.3',
    description='Base 36 utilities',
    url='http://www.ateijelo.com/',
    author='Andy Teijelo',
    author_email='ateijelo@gmail.com',
    packages=find_packages(),
    install_requires = [
        'python-baseconv'
    ],
    #package_data={
    #    '': ['schemas/*', 'templates/*'],
    #},
    tests_require = ['pytest'],
)
