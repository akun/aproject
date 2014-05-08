#!/usr/bin/env python


from setuptools import setup, find_packages
from pip.req import parse_requirements

def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]

from {{ cookiecutter.repo_name }} import VERSION


setup(
    name='{{ cookiecutter.project_name }}',
    version=VERSION,
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='MIT License',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    package_dir={'': '{{ cookiecutter.repo_name }}'},
    packages=find_packages('{{ cookiecutter.repo_name }}'),
    install_requires=get_reqs(),
    test_suite='nose.collector',
)
