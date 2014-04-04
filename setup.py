#!/usr/bin/env python


import os
import sys


from setuptools import setup, find_packages
from pip.req import parse_requirements
install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

from aproject import VERSION


setup(
    name='aproject',
    version=VERSION,
    description='A Project Template',
    author='akun',
    author_email='6awkun@gmail.com',
    license='MIT License',
    url='https://github.com/akun/aproject',
    package_dir={'': 'aproject'},
    packages=find_packages('aproject'),
    install_requires=reqs,
    test_suite='nose.collector',
)
