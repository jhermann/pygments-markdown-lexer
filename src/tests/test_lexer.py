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
    check(
        (Markdown.Markup, '# '),
        (Markdown.Heading, 'Header level 1'),
        (Text, '\n'),
    )
    check(
        (Markdown.Markup, '# '),
        (Markdown.Heading, 'Header level 1'),
        (Markdown.Markup, ' #'),
        (Text, '\n'),
    )
    check((Text, ' # not a header\n'),)
    for i in range(2, 6):
        check(
            (Markdown.Markup, '#' * i + ' '),
            (Markdown.SubHeading, 'H{n}'.format(n=i)),
            (Text, '\n'),
        )
        check(
            (Markdown.Markup, '#' * i + ' '),
            (Markdown.SubHeading, 'H{n}'.format(n=i)),
            (Markdown.Markup, ' ' + '#' * i),
            (Text, '\n'),
        )
        check((Text, ' {hashes} not a header\n'.format(n=i, hashes='#' * i)),)


def test_headings_using_underlining():
    check(
        (Markdown.Markup, '======\n'),
        (Markdown.SubHeading, 'Header\n'),
        (Markdown.Markup, '======'),
        (Text, '\ntext\n'),
    )
    check(
        (Markdown.Markup, '------\n'),
        (Markdown.SubHeading, 'Sub Header\n'),
        (Markdown.Markup, '------'),
        (Text, '\ntext\n'),
    )
    check((Text, '---- text ----\n'),)
    check((Text, '----\ntext ----\n'),)
    check((Text, 'text\n ----\n'),)
    check((Text, ' text\n----\n'),)


#############################################################################
### HTML

# TODO

def test_html_comments():
    check(
        (Text, 'abc '),
        (Markdown.Markup, '<!--'),
        (Markdown.HtmlComment, 'HTML - comment'),
        (Markdown.Markup, '-->'),
        (Text, 'def\n'),
    )


#############################################################################
### Other block / line elements

def test_horizontal_rules():
    check(
        (Text, 'abc\n\n_ _\n'),
    )
    check(
        (Text, 'abc\n'),
        (Markdown.Markup, '\n* '),
        (Text, '*\n'),
    )
    check(
        (Text, 'abc\n'),
        (Markdown.Markup, '\n- '),
        (Text, '-\n'),
    )
    for ch in '-*_':
        ch3 = ch * 3
        check((Text, 'abc {c} {c} {c} def\n'.format(c=ch)),)
        check((Text, ch + ch + '\n'),)
        check(
            (Text, 'abc\n'),
            (Markdown.Markup, '\n' + ch3 + '\n'),
            (Text, 'def\n'),
        )
        check(
            (Text, 'abc\n'),
            (Markdown.Markup, '\n{c} {c} {c}\n'.format(c=ch)),
            (Text, 'def\n'),
        )


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
            (Markdown.Markup, ch),
            (emph, 'ipsum dolor'),
            (Markdown.Markup, ch),
            (Text, ' sit amet\n'),
        )
        check(
            (Text, 'emphasized text '),
            (Markdown.Markup, ch),
            (emph, r'containing escaped markup (\{one_ch})'.format(one_ch=ch[0])),
            (Markdown.Markup, ch),
            (Text, '.\n'),
        )
        check(
            (Text, 'em'),
            (Markdown.Markup, ch),
            (emph, 'bedd'),
            (Markdown.Markup, ch),
            (Text, 'ed in words.\n'),
        )
        check(
            (Text, 'isolated{ch} with {ch} spaces\n'.format(ch=ch)),
        )


def test_lists_and_blockquotes():
    for lead in ('*', '+', '-', '1.', '21.', '>'):
        check(
            (Text, lead + 'Lorem ipsum.\n'),
        )
        check(
            (Markdown.Markup, lead + ' '),
            (Text, 'Lorem ipsum.\n'),
        )
        check(
            (Markdown.Markup, ' ' + lead + ' '),
            (Text, 'Lorem ipsum.\n'),
        )
        check(
            (Markdown.Markup, '\t' + lead + ' '),
            (Text, 'Lorem ipsum.\n'),
        )

def test_inline_code():
    check(
        (Markdown.Markup, r'``'),
        (Markdown.InlineCode, 'There is a literal backtick (`) here.'),
        (Markdown.Markup, r'``'),
        (Text, '\n'),
    )
