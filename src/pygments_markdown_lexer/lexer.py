# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Markdown lexer for Pygments.

    See `Write your own lexer`_ and `Builtin Tokens`_.

    .. _`Write your own lexer`: http://pygments.org/docs/lexerdevelopment/
    .. _`Builtin Tokens`: http://pygments.org/docs/tokens/
"""
# Copyright ©  2015 Jürgen Hermann <jh@web.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, unicode_literals, print_function

from pygments.lexer import RegexLexer
from pygments.token import *  # pylint: disable=wildcard-import, unused-wildcard-import

from ._compat import encode_filename


class MarkdownLexer(RegexLexer):
    """A Markdown lexer for Pygments."""
    name = 'Markdown'
    aliases = ['md', 'markdown']
    filenames = ['*.md', '*.mkd', '*.markdown']

    tokens = {
        encode_filename('root'): [
            # headings (hashmarks)
            (r'^# .+\n', Generic.Heading),
            (r'^#{2,5} .+\n', Generic.SubHeading),

            # emphasis (underscores)
            (r'(?<!_)_[^_ \t].*?(?<!\\|_| |\t)_(?!_)', Generic.Emph),

            # plain text
            (r'[-. A-Za-z0-9]+', Text),
        ]
    }
