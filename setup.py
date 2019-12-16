#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup.py"""

# pylint: disable=invalid-name
from __future__ import print_function
import sys
import ast
import os
from setuptools import setup, find_packages

#######################################################################
#                           Python Version                            #
#######################################################################
if sys.version_info.major != 3 or sys.version_info.minor < 6:
    sys.exit('Python version 3.6+ required!')

#######################################################################
#                             Package Name                            #
#######################################################################
libname = 'py2glsl'

#######################################################################
#                             Description                             #
#######################################################################
description = 'Create GLSL shaders using Python classes.'
long_description = '''{0}

Requires Python version 3.6 or newer.
'''.format(description)

#######################################################################
#                            Find Version                             #
#######################################################################
version = '0.0.unknown'

init_py_path = os.path.join('src', libname, '__init__.py')
version = '0.0.unknown'
try:
    with open(init_py_path) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            print(
                "WARNING: Version information not found in '{}', using placeholder '{}'"
                .format(init_py_path, version),
                file=sys.stderr
            )
except FileNotFoundError:
    print(
        "WARNING: Could not find file '{}', using placeholder version information '{}'"
        .format(init_py_path, version),
        file=sys.stderr
    )

#######################################################################
#                            Setup Method                             #
#######################################################################
setup(
    name=libname,
    description=description,
    long_description=long_description,
    version=version,
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'aenum',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
