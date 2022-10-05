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

from typing import TYPE_CHECKING, Any, List
from rply.token import BaseBox

if TYPE_CHECKING:
    from zed.state import ParserState

__all__ = (
    'BaseToken',
    'Program',
)


class BaseToken(BaseBox):
    r"""Base class for other AST assets.

    Parameters
    ----------
    state: :class:`ParserState`
        The parser state associated to the token.
    \*\*kwargs:
        The additional keyword arguments passed to token as metadata. These
        are handled by subclasses.

    Attributes
    ----------
    meta: Dict[:class:`str`, Any]
        The raw metadata passed as keyword while initializing
        the token.
    """
    def __init__(self, state: ParserState, **kwargs: Any) -> None:
        self.state = state
        self.meta = kwargs.copy()

    def eval(self) -> Any:
        """Evaluates the token.

        This method is meant to be implemented by subclasses and does
        nothing by default.
        """
        pass


class Program(BaseToken):
    """Represents the top level program.

    This contains other tokens in the program.

    Attributes
    ----------
    tokens:
        The list of other tokens in the program.
    """
    def __init__(self, state: ParserState, **kwargs: Any) -> None:
        super().__init__(state, **kwargs)

        self.tokens: List[BaseToken] = kwargs.pop('tokens')

    def eval(self):
        for token in self.tokens:
            token.eval()
