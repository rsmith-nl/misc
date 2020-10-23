# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-08-01T13:31:09+0200
# Last modified: 2019-08-08T23:05:41+0200
"""Group an iterator into sub-iterators."""

__version__ = "2019.08.08"

import itertools as it
import functools as ft


def chunked(iterable, n):  # {{{1
    """
    Split an iterable up in chunks of length n.

    The second argument to the outer ``iter()`` is crucial to the way this works.
    See the documentation for ``iter()`` for details.
    """

    def take(n, iterable):
        return list(it.islice(iterable, n))

    return iter(ft.partial(take, n, iter(iterable)), [])


# def chunked2(iterable, n):
#     """
#     Split an iterable up in chunks of length n.
#     (simple version)
#     """
#     itr = iter(iterable)
#     res = []
#     try:
#         while True:
#             for j in range(n):
#                 res.append(next(itr))
#             yield res
#             res = []
#     except StopIteration:
#         yield res
