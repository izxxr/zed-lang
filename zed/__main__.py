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

import argparse
import zed

parser = argparse.ArgumentParser(description='CLI for the Zed language')
parser.add_argument(
    'filename', help='The name of file to operate on.', type=str
)
parser.add_argument('--lex', help='Lex the file and output tokens rather than running it.', default=False)

args = parser.parse_args()

with open(args.filename, 'r') as f:
    source = f.read()
    lexer = zed.get_lexer()

    if args.lex:
        for token in lexer.lex(source):
            print(token)
    else:
        parser = zed.get_parser()
        try:
            parser.parse(lexer.lex(source), state=zed.ParserState()).eval()  # type: ignore
        except zed.CompilationError as error:
            print(error)
            exit()
