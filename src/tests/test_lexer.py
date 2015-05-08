# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, missing-docstring, no-self-use, bad-continuation
# pylint: disable=invalid-name, redefined-outer-name, too-few-public-methods
""" Test «pygments_markdown_lexer.lexer».
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

import pygments
#import pytest
from pygments.token import *  # pylint: disable=unused-wildcard-import

from pygments_markdown_lexer import lexer


def check(*expected):
    text = ''.join(i[1] for i in expected)
    md_lexer = lexer.MarkdownLexer()
    result = list(pygments.lex(text, md_lexer))
    assert result == list(expected)


def test_lexer_has_proper_name():
    md_lexer = lexer.MarkdownLexer()
    assert md_lexer.name == 'Markdown'
    assert 'md' in md_lexer.aliases
    assert 'markdown' in md_lexer.aliases


def test_multiple_lines_of_text():
    check(
        (Text, 'Lorem'),
        (Text, '\n'),
        (Text, 'ipsum dolor'),
        (Text, '\n'),
        (Text, 'sit amet.'),
        (Text, '\n'),
    )


def test_headings_using_hashmarks():
    check((Generic.Heading, '# Header level 1\n'),)
    for i in range(2, 6):
        check((Generic.SubHeading, '{hashes} H{n}\n'.format(n=i, hashes='#' * i)),)


def test_emphasis_with_underscores():
    check(
        (Text, 'Lorem '),
        (Generic.Emph, '_ipsum dolor_'),
        (Text, ' sit amet.'),
        (Text, '\n'),
    )
    check(
        (Text, 'emphasized text '),
        (Generic.Emph, r'_containing an underscore (\_)_'),
        (Text, '.'),
        (Text, '\n'),
    )
