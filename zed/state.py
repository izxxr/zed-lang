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

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from zed.ast.base import BaseToken


__all__ = (
    "ParserState",
)


class ParserState:
    """A class that maintains state of the Zed lang parser.

    An instance of this class is generally passed as first argument to
    production rules.
    """
    def __init__(self) -> None:
        self._current_stmts_list: List[BaseToken] = []
        self._definitions: Dict[str, Any] = {}

    def add_stmt(self, stmt: BaseToken) -> None:
        self._current_stmts_list.append(stmt)

    def eval_stmts(self) -> None:
        for stmt in self._current_stmts_list:
            stmt.eval()
        self._current_stmts_list.clear()

    def add_defn(self, ident: str, val: Any) -> None:
        self._definitions[ident] = val

    def get_defn(self, ident: str) -> Any:
        return self._definitions[ident]
