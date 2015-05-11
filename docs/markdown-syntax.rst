Markdown Syntax Examples
========================

The following are some pygmentized examples from the
`Markdown syntax reference`_.


.. _`Markdown syntax reference`: https://daringfireball.net/projects/markdown/syntax


.. code-block:: markdown

    <h2 id="overview">Overview</h2>

    <h3 id="philosophy">Philosophy</h3>

    <ul id="ProjectSubmenu">
        <li><a href="/projects/markdown/" title="Markdown Project Page">Main</a></li>
    </ul>

    HTML <!-- comment one-liner -->
    HTML <!-- comment
              on 2 lines -->
    This --> not a comment

.. code-block:: markdown

    *   [Overview](#overview)
        *   [Philosophy](#philosophy)
        *   [Inline HTML](#html)
        *   [Automatic Escaping for Special Characters](#autoescape)

    **Note:** This document is itself written using Markdown; you
    can [see the source for it by adding '.text' to the URL][src].

      [src]: /projects/markdown/syntax.text

.. code-block:: markdown

    * * *

.. code-block:: markdown

    … including [Setext] [1], [atx] [2], …

      [1]: http://docutils.sourceforge.net/mirror/setext.html
      [2]: http://www.aaronsw.com/2002/atx/

.. code-block:: markdown

    … *asterisks* around a word actually look like \*emphasis\*.

.. code-block:: markdown

    This is a regular paragraph.

    <table>
        <tr>
            <td>Foo</td>
        </tr>
    </table>

    This is another regular paragraph.

.. code-block:: markdown

    Span-level HTML tags -- e.g. `<span>`, `<cite>`, or `<del>` -- can be
    used anywhere in a Markdown paragraph, list item, or header.

.. code-block:: markdown

    Copyright symbol &copy;, but AT&T vs. AT&amp;T and 4 < 5.

.. code-block:: markdown

    This is a H1
    ============

        This is a H1
        ============

    This is a H2
    ------------

    Normal text.

.. code-block:: markdown

    # This is a H1

        # This is a H1

    ## This is a H2

    ###### This is a H6

    Normal text.

.. code-block:: markdown

    # This is a H1 #

        # This is a H1 #

    ## This is a H2 ##

    ### This is a H3 ######

    Normal text.


.. code-block:: markdown

        > This is a blockquote with two paragraphs. …
        >
        > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
        > id sem consectetuer libero luctus adipiscing.

        > This is a blockquote with only a leading indicator.

        > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
        id sem consectetuer libero luctus adipiscing.

    Blockquotes can be nested.

        > This is the first level of quoting.
        >
        > > This is nested blockquote.
        >
        > Back to the first level.

    Blockquotes can contain other Markdown elements, including headers, lists,
    and code blocks:

        > ## This is a header.
        >
        > 1.   This is the first list item.
        > 2.   This is the second list item.
        >
        > Here's some example code:
        >
        >     return shell_exec("echo $input | $markdown_script");


.. code-block:: markdown

    *   Red
    *   Green
    *   Blue

    +   Red
    +   Green
    +   Blue

    -   Red
    -   Green
    -   Blue

    1.  Bird
    2.  McHale
    3.  Parish

    *   A list item with a blockquote:

        > This is a blockquote
        > inside a list item.

    *   A list item with a code block:

            <code goes here>

    1986\. What a great season.


.. code-block:: markdown

    This is a normal paragraph:

        _This_ is a *code block*.

        * still code
        > also code

        tell application "Foo"
            beep
        end tell

    Regular Markdown syntax is not processed within code blocks.


.. code-block:: markdown

    You can produce a horizontal rule tag (`<hr />`) by placing three or
    more hyphens, asterisks, or underscores on a line by themselves. If you
    wish, you may use spaces between the hyphens or asterisks. Each of the
    following lines will produce a horizontal rule:

    * * *

    ***

    *****

    - - -

    ---------------------------------------


.. code-block:: markdown

    <h2 id="span">Span Elements</h2>

    <h3 id="link">Links</h3>

    Markdown supports two style of links: *inline* and *reference*.

    In both styles, the link text is delimited by [square brackets].

    To create an inline link, use a set of regular parentheses immediately
    after the link text's closing square bracket. Inside the parentheses,
    put the URL where you want the link to point, along with an *optional*
    title for the link, surrounded in quotes. For example:

        This is [an example](http://example.com/ "Title") inline link.

        [This link](http://example.net/) has no title attribute.

    Will produce:

        <p>This is <a href="http://example.com/" title="Title">
        an example</a> inline link.</p>

        <p><a href="http://example.net/">This link</a> has no
        title attribute.</p>

    If you're referring to a local resource on the same server, you can
    use relative paths:

        See my [About](/about/) page for details.

    Reference-style links use a second set of square brackets, inside
    which you place a label of your choosing to identify the link:

        This is [an example][id] reference-style link.

    You can optionally use a space to separate the sets of brackets:

        This is [an example] [id] reference-style link.

    Then, anywhere in the document, you define your link label like this,
    on a line by itself:

        [id]: http://example.com/  "Optional Title Here"

    That is:

    *   Square brackets containing the link identifier (optionally
        indented from the left margin using up to three spaces);
    *   followed by a colon;
    *   followed by one or more spaces (or tabs);
    *   followed by the URL for the link;
    *   optionally followed by a title attribute for the link, enclosed
        in double or single quotes, or enclosed in parentheses.

    The following three link definitions are equivalent:

        [foo]: http://example.com/  "Optional Title Here"
        [foo]: http://example.com/  'Optional Title Here'
        [foo]: http://example.com/  (Optional Title Here)

    **Note:** There is a known bug in Markdown.pl 1.0.1 which prevents
    single quotes from being used to delimit link titles.

    The link URL may, optionally, be surrounded by angle brackets:

        [id]: <http://example.com/>  "Optional Title Here"

    You can put the title attribute on the next line and use extra spaces
    or tabs for padding, which tends to look better with longer URLs:

        [id]: http://example.com/longish/path/to/resource/here
            "Optional Title Here"

    Link definitions are only used for creating links during Markdown
    processing, and are stripped from your document in the HTML output.

    Link definition names may consist of letters, numbers, spaces, and
    punctuation -- but they are *not* case sensitive. E.g. these two
    links:

        [link text][a]
        [link text][A]

    are equivalent.

    The *implicit link name* shortcut allows you to omit the name of the
    link, in which case the link text itself is used as the name.
    Just use an empty set of square brackets -- e.g., to link the word
    "Google" to the google.com web site, you could simply write:

        [Google][]

    And then define the link:

        [Google]: http://google.com/

    Because link names may contain spaces, this shortcut even works for
    multiple words in the link text:

        Visit [Daring Fireball][] for more information.

    And then define the link:

        [Daring Fireball]: http://daringfireball.net/

    Link definitions can be placed anywhere in your Markdown document. I
    tend to put them immediately after each paragraph in which they're
    used, but if you want, you can put them all at the end of your
    document, sort of like footnotes.

    Here's an example of reference links in action:

        I get 10 times more traffic from [Google] [1] than from
        [Yahoo] [2] or [MSN] [3].

          [1]: http://google.com/        "Google"
          [2]: http://search.yahoo.com/  "Yahoo Search"
          [3]: http://search.msn.com/    "MSN Search"

    Using the implicit link name shortcut, you could instead write:

        I get 10 times more traffic from [Google][] than from
        [Yahoo][] or [MSN][].

          [google]: http://google.com/        "Google"
          [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
          [msn]:    http://search.msn.com/    "MSN Search"

    Both of the above examples will produce the following HTML output:

        <p>I get 10 times more traffic from <a href="http://google.com/"
        title="Google">Google</a> than from
        <a href="http://search.yahoo.com/" title="Yahoo Search">Yahoo</a>
        or <a href="http://search.msn.com/" title="MSN Search">MSN</a>.</p>

    For comparison, here is the same paragraph written using
    Markdown's inline link style:

        I get 10 times more traffic from [Google](http://google.com/ "Google")
        than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
        [MSN](http://search.msn.com/ "MSN Search").

    The point of reference-style links is not that they're easier to
    write. The point is that with reference-style links, your document
    source is vastly more readable. Compare the above examples: using
    reference-style links, the paragraph itself is only 81 characters
    long; with inline-style links, it's 176 characters; and as raw HTML,
    it's 234 characters. In the raw HTML, there's more markup than there
    is text.

    With Markdown's reference-style links, a source document much more
    closely resembles the final output, as rendered in a browser. By
    allowing you to move the markup-related metadata out of the paragraph,
    you can add links without interrupting the narrative flow of your
    prose.


    <h3 id="em">Emphasis</h3>

    Markdown treats asterisks (`*`) and underscores (`_`) as indicators of
    emphasis. Text wrapped with one `*` or `_` will be wrapped with an
    HTML `<em>` tag; double `*`'s or `_`'s will be wrapped with an HTML
    `<strong>` tag. E.g., this input:

        *single asterisks*

        _single underscores_

        **double asterisks**

        __double underscores__

    will produce:

        <em>single asterisks</em>

        <em>single underscores</em>

        <strong>double asterisks</strong>

        <strong>double underscores</strong>

    You can use whichever style you prefer; the lone restriction is that
    the same character must be used to open and close an emphasis span.

    Emphasis can be used in the middle of a word:

        un*frigging*believable

    But if you surround an `*` or `_` with spaces, it'll be treated as a
    literal asterisk or underscore.

    To produce a literal asterisk or underscore at a position where it
    would otherwise be used as an emphasis delimiter, you can backslash
    escape it:

        \*this text is surrounded by literal asterisks\*



    <h3 id="code">Code</h3>

    To indicate a span of code, wrap it with backtick quotes (`` ` ``).
    Unlike a pre-formatted code block, a code span indicates code within a
    normal paragraph. For example:

        Use the `printf()` function.

    will produce:

        <p>Use the <code>printf()</code> function.</p>

    To include a literal backtick character within a code span, you can use
    multiple backticks as the opening and closing delimiters:

        ``There is a literal backtick (`) here.``

    which will produce this:

        <p><code>There is a literal backtick (`) here.</code></p>

    The backtick delimiters surrounding a code span may include spaces --
    one after the opening, one before the closing. This allows you to place
    literal backtick characters at the beginning or end of a code span:

        A single backtick in a code span: `` ` ``

        A backtick-delimited string in a code span: `` `foo` ``

    will produce:

        <p>A single backtick in a code span: <code>`</code></p>

        <p>A backtick-delimited string in a code span: <code>`foo`</code></p>

    With a code span, ampersands and angle brackets are encoded as HTML
    entities automatically, which makes it easy to include example HTML
    tags. Markdown will turn this:

        Please don't use any `<blink>` tags.

    into:

        <p>Please don't use any <code>&lt;blink&gt;</code> tags.</p>

    You can write this:

        `&#8212;` is the decimal-encoded equivalent of `&mdash;`.

    to produce:

        <p><code>&amp;#8212;</code> is the decimal-encoded
        equivalent of <code>&amp;mdash;</code>.</p>



    <h3 id="img">Images</h3>

    Admittedly, it's fairly difficult to devise a "natural" syntax for
    placing images into a plain text document format.

    Markdown uses an image syntax that is intended to resemble the syntax
    for links, allowing for two styles: *inline* and *reference*.

    Inline image syntax looks like this:

        ![Alt text](/path/to/img.jpg)

        ![Alt text](/path/to/img.jpg "Optional title")

    That is:

    *   An exclamation mark: `!`;
    *   followed by a set of square brackets, containing the `alt`
        attribute text for the image;
    *   followed by a set of parentheses, containing the URL or path to
        the image, and an optional `title` attribute enclosed in double
        or single quotes.

    Reference-style image syntax looks like this:

        ![Alt text][id]

    Where "id" is the name of a defined image reference. Image references
    are defined using syntax identical to link references:

        [id]: url/to/image  "Optional title attribute"

    As of this writing, Markdown has no syntax for specifying the
    dimensions of an image; if this is important to you, you can simply
    use regular HTML `<img>` tags.


    * * *


    <h2 id="misc">Miscellaneous</h2>

    <h3 id="autolink">Automatic Links</h3>

    Markdown supports a shortcut style for creating "automatic" links for URLs and email addresses: simply surround the URL or email address with angle brackets. What this means is that if you want to show the actual text of a URL or email address, and also have it be a clickable link, you can do this:

        <http://example.com/>

    Markdown will turn this into:

        <a href="http://example.com/">http://example.com/</a>

    Automatic links for email addresses work similarly, except that
    Markdown will also perform a bit of randomized decimal and hex
    entity-encoding to help obscure your address from address-harvesting
    spambots. For example, Markdown will turn this:

        <address@example.com>

    into something like this:

        <a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
        &#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
        &#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
        &#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>

    which will render in a browser as a clickable link to "address@example.com".

    (This sort of entity-encoding trick will indeed fool many, if not
    most, address-harvesting bots, but it definitely won't fool all of
    them. It's better than nothing, but an address published in this way
    will probably eventually start receiving spam.)



    <h3 id="backslash">Backslash Escapes</h3>

    Markdown allows you to use backslash escapes to generate literal
    characters which would otherwise have special meaning in Markdown's
    formatting syntax. For example, if you wanted to surround a word
    with literal asterisks (instead of an HTML `<em>` tag), you can use
    backslashes before the asterisks, like this:

        \*literal asterisks\*

    Markdown provides backslash escapes for the following characters:

        \   backslash
        `   backtick
        *   asterisk
        _   underscore
        {}  curly braces
        []  square brackets
        ()  parentheses
        #   hash mark
        +    plus sign
        -    minus sign (hyphen)
        .   dot
        !   exclamation mark
