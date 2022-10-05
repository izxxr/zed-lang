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

"""This module implements parsing logic for Zed lang.

The main components of this module are:

- get_parser()   : Returns the rply.LRParser instance used for parsing the lexed code.
- reset_parser() : Resets the cached parser such that get_parser() recreates the parser
                   instead of returning the cached value.
- CompilationError : An exception raised when compilation fails.


For more information regarding a specific function, read the documentation for
that function.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Mapping
from zed.sentinels import UNDEFINED
from zed import lexer, ast

import rply

if TYPE_CHECKING:
    from rply.parser import LRParser
    from rply.token import SourcePosition
    from zed.state import ParserState

    Tokens = List[rply.Token]


__all__ = (
    "get_parser",
    "reset_parser",
    "CompilationError",
)


_parser: Optional[LRParser] = None
_pg: rply.ParserGenerator = rply.ParserGenerator(list(lexer.get_tokens()))


def get_parser() -> LRParser:
    """Constructs the rply.LRParser instance for parsing the lexed code.

    On repeated calls, this function will return a cached value. For resetting
    this cached value, use reset_parser() function.
    """
    global _parser
    if _parser:
        return _parser

    _parser = _pg.build()
    return _parser

def reset_parser() -> None:
    """Resets the parser cache.

    After this function has been called, calling get_parser() will construct
    a completely new parser instance rather than returning a cached instance.
    """
    global _parser
    _parser = None


class CompilationError(Exception):
    """An error raised when compilation fails."""
    def __init__(self, pos: Optional[SourcePosition], message: str) -> None:
        self.pos = pos
        self.message = message

        if pos:
            error = "At line %r, column %r, position %r\nerror: %s" % \
                     (pos.lineno, pos.colno, pos.idx, message)
        else:
            error = message

        super().__init__(error)


@_pg.production('prog : stmt_list')
def prod_prog(state: ParserState, tokens: Tokens):
    return ast.Program(state, tokens=tokens)

@_pg.production('stmt_list : stmt')
@_pg.production('stmt_list : stmt_list stmt')
def prod_stmt(state: ParserState, tokens: Tokens):
    if len(tokens) == 1:
        stmt = tokens[0]
    else:
        stmt = tokens[1]

    state.add_stmt(stmt)  # type: ignore
    return ast.Statements(state)

@_pg.production('expr : IDENT')
@_pg.production('expr : LT_STRING')
@_pg.production('expr : LT_UNDEFINED')
def prod_expr_string(state: ParserState, tokens: Tokens):
    token = tokens[0]
    tokentp = token.gettokentype()

    if tokentp == 'LT_UNDEFINED':
        return ast.Undefined(state)
    if tokentp == 'LT_STRING':
        # [1:-1] is needed to dequote the string
        return ast.String(state, value=token.getstr()[1:-1])
    if tokentp == 'IDENT':
        ident = token.getstr()
        try:
            value = state.get_defn(ident)
        except KeyError:
            raise CompilationError(token.getsourcepos(), 'identifier %r not defined' % ident)
        else:
            return value

    raise AssertionError('Unknown token type for expr')

@_pg.production('stmt : STMT_PRINT expr')
def prod_stmt_print(state: ParserState, tokens: Tokens):
    return ast.Print(state, value=tokens[1])

@_pg.production('stmt : STMT_LET IDENT OP_ASSIGN expr')
@_pg.production('stmt : STMT_LET IDENT')
def prod_stmt_let(state: ParserState, tokens: Tokens):
    ident = tokens[1].getstr()
    if len(tokens) == 2:
        value = UNDEFINED
    else:
        value = tokens[3]

    state.add_defn(ident, value)  # type: ignore
    return ast.Let(state, ident=ident, value=value)
