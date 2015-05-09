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

from pygments_markdown_lexer.lexer import Markdown, MarkdownLexer


#############################################################################
### Helpers

def check(*expected):
    text = ''.join(i[1] for i in expected)
    md_lexer = MarkdownLexer()
    md_lexer.add_filter('raiseonerror')
    md_lexer.add_filter('tokenmerge')
    result = list(pygments.lex(text, md_lexer))
    assert result == list(expected)


#############################################################################
### Basics

def test_lexer_has_proper_name():
    md_lexer = MarkdownLexer()
    assert md_lexer.name == 'Markdown'
    assert 'md' in md_lexer.aliases
    assert 'markdown' in md_lexer.aliases


def test_multiple_lines_of_text():
    check((Text, 'Lorem\nipsum dolor\nsit amet.\n'),)


#############################################################################
### Headings

def test_headings_using_hashmarks():
    check((Markdown.Heading, '# Header level 1\n'),)
    check((Markdown.Heading, '# Header level 1 #\n'),)
    check((Text, ' # not a header\n'),)
    for i in range(2, 6):
        check((Markdown.SubHeading, '{hashes} H{n}\n'.format(n=i, hashes='#' * i)),)
        check((Markdown.SubHeading, '{hashes} H{n} {hashes}\n'.format(n=i, hashes='#' * i)),)
        check((Text, ' {hashes} not a header\n'.format(n=i, hashes='#' * i)),)


def test_headings_using_underlining():
    check(
        (Markdown.Heading, '======\nHeader\n======\n'),
        (Text, 'text\n'),
    )
    check(
        (Markdown.SubHeading, '------\nSub Header\n------\n'),
        (Text, 'text\n'),
    )
    check((Text, '---- text ----\n'),)
    check((Text, '----\ntext ----\n'),)
    check((Text, 'text\n ----\n'),)
    check((Text, ' text\n----\n'),)


#############################################################################
### HTML

# TODO


#############################################################################
### Inline

def test_escape_by_backslash():
    check(
        (String.Escape, r'\*'),
        (Text, 'bold'),
        (String.Escape, r'\*'),
        (Text, ' '),
        (String.Escape, r'\`'),
        (Text, 'code'),
        (String.Escape, r'\`'),
        (Text, '\n'),
    )


def test_html_entities():
    check(
        (Text, 'Copyright symbol '),
        (Markdown.HtmlEntity, '&copy;'),
        (Text, 'but AT&T vs. AT'),
        (Markdown.HtmlEntity, '&amp;'),
        (Text, 'T and 4 < 5.\n'),
    )
    check(
        (Text, 'a '),
        (String.Escape, r'\&'),
        (Text, ' z\n'),
    )


def test_emphasis_with_underscore_and_asterisk():
    data = (
        (Generic.Emph, '_'), (Generic.Emph, '*'),
        (Generic.Strong, '__'), (Generic.Strong, '**'),
    )
    for emph, ch in data:
        check(
            (Text, 'Lorem '),
            (emph, '{ch}ipsum dolor{ch}'.format(ch=ch)),
            (Text, ' sit amet\n'),
        )
        check(
            (Text, 'emphasized text '),
            (emph, r'{ch}containing escaped markup (\{one_ch}){ch}'.format(ch=ch, one_ch=ch[0])),
            (Text, '.\n'),
        )
        check(
            (Text, 'em'),
            (emph, '{ch}bedd{ch}'.format(ch=ch)),
            (Text, 'ed in words.\n'),
        )
        check(
            (Text, 'isolated{ch} with {ch} spaces\n'.format(ch=ch)),
        )
