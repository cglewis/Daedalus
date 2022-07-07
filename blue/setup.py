#!/usr/bin/env python
from setuptools import setup

setup(
    name='daedalus-5g',
    setup_requires=['setuptools>=17.1'],
    python_requires='>=3.6',
    packages=['daedalus'],
    package_dir={'daedalus': '5G/daedalus'},
    py_modules=['daedalus'],
)
