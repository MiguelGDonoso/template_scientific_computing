#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.rst', 'r') as fobj:
    long_description = fobj.read()

setup(
    name='project',
    version='0.0.0',
    description='Project description.',
    license='BSD-2-Clause',
    long_description=long_description,
    author='Miguel Gómez Donoso',
    author_email='miguelgdonoso@gmail.com',
    url='https://pymbook.readthedocs.io/en/latest/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.5',
    install_requires=['numpy', 'matplotlib', 'scipy']
)
