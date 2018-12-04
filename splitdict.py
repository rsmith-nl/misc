# file: splitdict.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-12-04T00:08:57+0100
# Last modified: 2018-12-04T00:18:19+0100


def splitdict(words):
    """Split a string of whitespace delimited words or a list/tuple of words
    into a dict definition.

    >>> splitdict('spam eggs foo bar')
    "{'spam': spam, 'eggs': eggs, 'foo': foo, 'bar': bar}"
    """
    if isinstance(words, str):
        items = words.strip().split()
    elif type(words) in (list, tuple):
        items = [w.strip() for w in words]
    return '{' + ', '.join([f"'{item}': {item}" for item in items]) + '}'
