#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test script for PyQt5 support.
"""
import sys
# pylint: disable=import-error
from py2glsl.gl_provider.pyqt5 import PyQt5OpenGLProvider

def main():
    prov = PyQt5OpenGLProvider()
    prov.main(sys.argv)

if __name__ == "__main__":
    main()
