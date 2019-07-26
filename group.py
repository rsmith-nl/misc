# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-08-01T13:31:09+0200
# Last modified: 2019-07-26T23:36:56+0200
"""Group an iterator into sub-iterators."""

__version__ = '0.3'

import itertools as it
import functools as ft


def chunked(iterable, n):  # {{{1
    def take(n, iterable):
        return list(it.islice(iterable, n))
    return iter(ft.partial(take, n, iter(iterable)), [])
