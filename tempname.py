# file: tempname.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2013-11-11 22:47:29 +0100
# Last modified: 2016-03-20 12:55:33 +0100
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to tempname.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Module to create a temporary filename."""

import base64
import os


def tempname(ext=None, num=None):
    """Create a name for a temporary file.

    Arguments:
        ext: Optional extension to give to the file.
        num: Optional number suffix.

    Returns:
        Name for a temporary file.
    """
    bn = base64.b64encode(os.urandom(12), b'__').decode()
    if num is not None and num > 0:
        bn += '-{:03d}'.format(num)
    if ext:
        if not ext.startswith('.'):
            ext = '.' + ext
        bn += ext
    return bn


if __name__ == '__main__':
    print(tempname())
    print(tempname('foo'))
