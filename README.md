# pygments-markdown-lexer

A Markdown lexer for Pygments to highlight Markdown code snippets.

 [![Travis CI](https://api.travis-ci.org/jhermann/pygments-markdown-lexer.svg)](https://travis-ci.org/jhermann/pygments-markdown-lexer)
 [![Coveralls](https://img.shields.io/coveralls/jhermann/pygments-markdown-lexer.svg)](https://coveralls.io/r/jhermann/pygments-markdown-lexer)
 [![GitHub Issues](https://img.shields.io/github/issues/jhermann/pygments-markdown-lexer.svg)](https://github.com/jhermann/pygments-markdown-lexer/issues)
 [![License](https://img.shields.io/pypi/l/pygments-markdown-lexer.svg)](https://github.com/jhermann/pygments-markdown-lexer/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/pygments-markdown-lexer/badge.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)
 [![Latest Version](https://img.shields.io/pypi/v/pygments-markdown-lexer.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)
 [![Download format](https://pypip.in/format/pygments-markdown-lexer/badge.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)
 [![Downloads](https://img.shields.io/pypi/dw/pygments-markdown-lexer.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)


## Overview

…


## Installation

*Pygments Markdown Lexer* can be installed via ``pip install pygments-markdown-lexer`` as usual,
see [releases](https://github.com/jhermann/pygments-markdown-lexer/releases) for an overview of available versions.
To get a bleeding-edge version from source, use these commands:

```sh
repo="jhermann/pygments-markdown-lexer"
pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"
```

See [Contributing](#contributing) on how to create a full development environment.


## Usage

…


## Contributing

To create a working directory for this project, call these commands:

```sh
git clone "https://github.com/jhermann/pygments-markdown-lexer.git"
cd "pygments-markdown-lexer"
. .env --yes --develop
invoke build --docs test check
```

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See [CONTRIBUTING](https://github.com/jhermann/pygments-markdown-lexer/blob/master/CONTRIBUTING.md) for more.


## References

**Tools**

* [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.org/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [twine](https://github.com/pypa/twine#twine)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)


## Acknowledgements

…
