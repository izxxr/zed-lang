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
from zed.sentinels import UNDEFINED
from zed.ast.base import BaseToken

if TYPE_CHECKING:
    from zed.state import ParserState

__all__ = (
    'String',
    'Undefined',
)


class String(BaseToken):
    """Represents a string literal.

    Attributes
    ----------
    value: :class:`str`
        The string literal.
    """
    def __init__(self, state: ParserState, **kwargs: Any) -> None:
        super().__init__(state, **kwargs)

        self.value = kwargs.pop('value')

    def eval(self):
        return self.value


class Undefined(BaseToken):
    """Represents an undefined literal."""
    def __init__(self, state: ParserState, **kwargs: Any) -> None:
        super().__init__(state, **kwargs)

    def eval(self):
        return UNDEFINED
