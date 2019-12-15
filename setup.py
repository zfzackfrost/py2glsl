#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup.py"""

import sys
from setuptools import setup, find_packages

if sys.version_info.major != 3 or sys.version_info.minor < 6:
    sys.exit('Python version 3.6+ required!')

setup(
    name='py2glsl',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'aenum',
        'numpy',
    ]
)
