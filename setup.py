#!/usr/bin/env python
# -*- coding: utf8 -*-

"""setup.py file for marc2rf."""

# Import required modules
import re
from distutils.core import setup
import py2exe

__author__ = 'Victoria Morris'
__license__ = 'MIT License'
__version__ = '1.0.0'
__status__ = '4 - Beta Development'

# Determine version by reading __init__.py
version = re.search("^__version__\s*=\s*'(.*)'",
                    open('marc2rf/__init__.py').read(),
                    re.M).group(1)

# Get long description by reading README.md
try:
    long_description = open('README.md').read()
except:
    long_description = ''

# List requirements.
# All other requirements should all be contained in the standard library
requirements = [
    'py2exe',
    'regex'
]

# Setup
setup(
    console=[
        'bin/write_rf_config.py',
        'bin/researcherFormat.py',
    ],
    zipfile=None,
    options={
        'py2exe': {
            'bundle_files': 0,
        }
    },
    name='marc2rf',
    version=version,
    author='Victoria Morris',
    url='https://github.com/victoriamorris/marc2rf',
    license='MIT',
    description='Tools for converting MARC records to Researcher Format.',
    long_description=long_description,
    packages=['marc2rf'],
    scripts=[
        'bin/write_rf_config.py',
        'bin/researcherFormat.py',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python'
    ],
    requires=requirements
)
