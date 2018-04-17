# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-08-01T13:31:09+0200
# Last modified: 2018-04-17T20:48:39+0200
"""Group an interator into sub-iterators."""

__version__ = '0.1.1'


def subgroup(it, n):  # {{{1
    """Split an iterator into a list of sub-iterators of size n.

    Arguments:
        it: Iterator to divide
        n: Length of sub-iterators

    Returns:
        A list of sub-iterators.
    """
    return [it[i:i+n] for i in range(0, len(it), n)]


if __name__ == '__main__':  # Test {{{1
    f = range(10)
    print('Test for group.py')
    print('f:', f)
    print('subgroup(f, 3):', subgroup(f, 3))
