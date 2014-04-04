#!/usr/bin/env python


from setuptools import setup, find_packages
from pip.req import parse_requirements

def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]

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
    install_requires=get_reqs(),
    test_suite='nose.collector',
)
