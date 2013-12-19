#!/usr/bin/env python


import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from aproject import VERSION


setup(
    name='aproject',
    version=VERSION,
    description='A Project Template',
    author='akun',
    url='https://github.com/akun/aproject',
    packages=[
        'aproject',
    ],
    package_dir={'aproject': 'aproject'},
    install_requires=[
        'Django==1.5.5',
        'nose==1.3.0',
        'Sphinx==1.1.3',
    ],
    test_suite='nose.collector',
)
