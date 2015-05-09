# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation, too-few-public-methods
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

import re

from pygments.lexer import RegexLexer, include, bygroups, using, this, do_insertions, default, words
from pygments.token import *  # pylint: disable=wildcard-import, unused-wildcard-import

from ._compat import encode_filename as state


class Markdown(object):
    """Symbolic names for Markdown tokens."""
    Heading = Generic.Heading
    SubHeading = Generic.Heading
    CodeBlock = Comment.Preproc
    HtmlSingle = Comment.Single
    HtmlBlock = Comment.Special
    HtmlEntity = String.Symbol


class MarkdownLexer(RegexLexer):
    """
        A Markdown lexer for Pygments.

        Some rules adapted from code in ``pygments.lexers.markup`` (BSD-licensed).
    """
    name = 'Markdown'
    aliases = ['md', 'markdown']
    filenames = ['*.md', '*.mkd', '*.markdown']
    mimetypes = ["text/x-markdown"]
    flags = re.MULTILINE

    # from docutils.parsers.rst.states
    closers = u'\'")]}>\u2019\u201d\xbb!?'
    unicode_delimiters = u'\u2010\u2011\u2012\u2013\u2014\u00a0'
    end_string_suffix = (r'((?=$)|(?=[-/:.,; \n\x00%s%s]))'
                         % (re.escape(unicode_delimiters),
                            re.escape(closers)))

    tokens = {
        state('root'): [
            # Headings (hashmarks)
            (r'^# .+( #)?\n', Markdown.Heading),
            (r'^#{2,6} .+( #{2,6})?\n', Markdown.SubHeading),

            # Headings (underlined)
            (r'^(={3,}\n)?\S.{2,}\n={3,}\n', Markdown.Heading),
            (r'^(-{3,}\n)?\S.{2,}\n-{3,}\n', Markdown.SubHeading),

            # HTML one-liners
            (r'^<(?P<tag>[-:a-zA-Z0-9]+)( [^>]+)>.+</(?P=tag)>\n', Markdown.HtmlSingle),

            # HTML blocks
            (r'^<[^/>][^>]*>\n', Markdown.HtmlBlock, state('htmlblock')),

            # GitHub style code blocks
            (r'^(```)(.*?)(\n)',
             bygroups(Name.Builtin, Name.Namespace, Markdown.CodeBlock),
             state('codeblock')),

            include(state('inline')),
        ],
        state('inline'): [
            # Escaping (before everything else)
            (r'\\.', String.Escape),

            # HTML entities
            (r'&[-a-z0-9]+;', Markdown.HtmlEntity),
            (r'&#[0-9]{1,9};', Markdown.HtmlEntity),
            (r'&', Text),

            # Inline code
            (r'``?', String.Backtick, state('literal')),

            # Emphasis
            (r'_?_[ \n]', Text),  # whitespace escape
            (r'\*?\*[ \n]', Text),  # whitespace escape
            (r'\*\*.+?(?<![ \\])\*\*', Generic.Strong),
            (r'__.+?(?<![ \\])__', Generic.Strong),
            (r'\*.+?(?<![ \\])\*', Generic.Emph),
            (r'_.+?(?<![ \\])_', Generic.Emph),

            #(r'(`.+?)(<.+?>)(`__?)',  # reference with inline target
            # bygroups(String, String.Interpol, String)),
            #(r'`.+?`__?', String),  # reference
            #(r'(`.+?`)(:[a-zA-Z0-9:-]+?:)?',
            # bygroups(Name.Variable, Name.Attribute)),  # role
            #(r'(:[a-zA-Z0-9:-]+?:)(`.+?`)',
            # bygroups(Name.Attribute, Name.Variable)),  # role (content first)
            #(r'\[.*?\]_', String),  # Footnote or citation
            #(r'<.+?>', Name.Tag),   # Hyperlink
            #(r'[^\\\n\[*`:]+', Text),

            # Remaining text
            (r'[a-zA-Z0-9]+', Text),  # optimize normal words a little
            (r'.', Text),  # default fallback
        ],
        state('literal'): [
            (r'[^`]+', String.Backtick),
            (r'(?<!\\)``?' + end_string_suffix, String.Backtick, state('#pop')),
        ],
        state('htmlblock'): [  # TODO: delegate to HTML lexer
            (r'^</[^>]+>\n', Markdown.HtmlBlock, state('#pop')),
            (r'.*\n', Markdown.HtmlBlock),  # slurp boring text
        ],
        state('codeblock'): [
            (r'^```\n', Name.Builtin, state('#pop')),
            (r'[^`]+', Markdown.CodeBlock),  # slurp boring text
            (r'`', Markdown.CodeBlock),  # allow single backticks
        ],
    }
