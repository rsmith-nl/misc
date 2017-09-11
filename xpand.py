# file: xpand.py
# vim:fileencoding=utf-8:ft=python:fmd=marker
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2013-08-13 23:13:48 +0200
# Last modified: 2017-09-11 02:49:55 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to xpand.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Function to expand filename globs."""

import glob


def xpand(args):  # {{{1
    """Expand command line arguments for operating systems incapable of doing
    so.

    Arguments:
        args: String or list of strings.

    Returns:
        Expanded argument list of strings.
    """
    if isinstance(args, str):
        args = [args]
    xa = []
    for a in args:
        g = glob.glob(a)
        if g:
            xa += g
        else:
            xa += [a]
    return xa
