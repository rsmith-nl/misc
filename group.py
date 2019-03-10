# file: group.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-08-01T13:31:09+0200
# Last modified: 2019-03-10T21:10:28+0100
"""Group an interator into sub-iterators."""

__version__ = '0.2'


def chunks(sequence, count):  # {{{1
    """Split an sequence into chunks of count items."""
    if count < 1:
        raise ValueError('count must be > 0')
    for i in range(0, len(sequence), count):
        yield sequence[i:i+count]


if __name__ == '__main__':  # Test {{{1
    f = range(10)
    print('Test for group.py')
    print('f:', f)
    print('chunks(f, 3):', chunks(f, 3))
