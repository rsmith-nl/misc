# file: xpand.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2013-2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2013-08-13T23:13:48+0200
# Last modified: 2018-04-17T20:45:41+0200
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
