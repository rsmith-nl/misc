# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-08-01T13:31:09+0200
# Last modified: 2024-06-09T17:31:05+0200
"""Group an iterator into sub-iterators."""

__version__ = "2019.08.08"

import itertools as it
import functools as ft


def chunked(iterable, n):  # {{{1
    """
    Split an iterable up in chunks of length n.

    The second argument to the outer ``iter()`` is crucial to the way this works.
    See the documentation for ``iter()`` for details.

    Example:
    >>> from group import chunked
    >>> list(chunked(range(10), 4))
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
    """

    def take(n, iterable):
        return list(it.islice(iterable, n))

    return iter(ft.partial(take, n, iter(iterable)), [])
