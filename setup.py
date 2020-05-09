#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.rst', 'r') as fobj:
    long_description = fobj.read()

setup(
    name='{project_name}',
    version='0.0.0',
    license='BSD-2-Clause',
    description='{project_description}',
    long_description=long_description,
    author='Miguel Gómez Donoso',
    author_email='miguelgdonoso@gmail.com',
    url='{project_repository_url}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: BSD License',
    ],
    keywords=['{keywords}'],
    python_requires='>=3.5',
    install_requires=['numpy', 'matplotlib', 'scipy']
)
