# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-08-01 13:31:09 +0200
# Last modified: 2017-09-11 02:41:03 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to group.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/
"""Group an interator into sub-iterators."""

__version__ = '0.1.1'


def group(it, n):  # {{{1
    """Group an iterator into a list of sub-iterators of size n.

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
    print('group(f, 3):', group(f, 3))
