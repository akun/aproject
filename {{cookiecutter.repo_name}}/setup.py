#!/usr/bin/env python


from setuptools import setup, find_packages
from pip.req import parse_requirements

from {{ cookiecutter.repo_name }} import VERSION


def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]


setup(
    name='{{ cookiecutter.project_name }}',
    version=VERSION,
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='MIT License',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six>=1.9.0',
    ],
    extras_require={
        'dev': [
            'prospector>=0.10.2',
        ],
        'test': [
            'coverage>=3.7.1',
            'coveralls>=0.5',
            'nose>=1.3.7',
            'python-coveralls>=2.5.0',
        ],
        'docs': [
            'Sphinx>=1.3.1',
        ],
    },
    test_suite='nose.collector',
)
