"""
Zed Programming Language
~~~~~~~~~~~~~~~~~~~~~~~~

A simple and experimental programming language written in Python. For
more information, see project repository at https://github.com/nerdguyahmad/zed-lang

License: MIT
Author: Izhar Ahmad
"""

__version__ = '0.1.0-alpha1'
__license__ = 'MIT'
__author__ = 'Izhar Ahmad'

from zed import ast as ast
from zed.lexer import *
from zed.parser import *
from zed.state import *
