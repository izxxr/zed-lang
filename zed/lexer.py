# MIT License

# Copyright (c) 2022 I. Ahmad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module specifies lexer and lexical tokens for Zed lang.

Lexer is used for lexical analysis for producing parseable tokens. Lexer
is powered by rply lexer generator.

The main components of this module are:

- get_tokens()  : Returns a mapping of language token to token patterns.
- get_lexer()   : Returns the rply.Lexer instance used for lexing the code.
- reset_lexer() : Resets the cached lexer such that get_lexer() recreates the lexer
                  instead of returning the cached value.

For more information regarding a specific function, read the documentation for
that function.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional, Tuple, Mapping
import rply

if TYPE_CHECKING:
    from rply.lexer import Lexer

__all__ = (
    "get_tokens",
    "get_lexer",
    "reset_lexer",
)


_lexer: Optional[Lexer] = None


def get_tokens() -> Mapping[str, str]:
    """Returns a mapping tokens used for lexing the source code.

    The key of mapping is a string representing the token type
    and value represents the regular expression pattern for
    matching that token.
    """
    return TOKENS.copy()

def get_lexer() -> Lexer:
    """Constructs the rply.Lexer instance for lexical analysis of source code.

    On repeated calls, this function will return a cached value. For resetting
    this cached value, use reset_lexer() function.
    """
    global _lexer
    if _lexer:
        return _lexer

    lg = rply.LexerGenerator()

    for token, pattern in TOKENS.items():
        lg.add(token, pattern)
    for token in IGNORED_TOKENS:
        lg.ignore(token)

    _lexer = lg.build()

    return _lexer

def reset_lexer() -> None:
    """Resets the lexer cache.

    After this function has been called, calling get_lexer() will construct
    a completely new lexer instance rather than returning a cached instance.
    """
    global _lexer
    _lexer = None


IGNORED_TOKENS: Tuple[str, ...] = (r'\s+',)
TOKENS: Dict[str, str] = {
    # Literals
    'LT_STRING': r'(".+")|(\'.+\')|(\'\')|("")',

    # Statements
    'STMT_PRINT': 'print',
}
