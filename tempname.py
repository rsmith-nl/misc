# file: tempname.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2013-11-11T22:47:29+0100
# Last modified: 2018-07-08T11:37:40+0200
"""Module to create a temporary filename."""

import base64
import os


def tempname(ext=None, num=None):  # {{{1
    """Create a name for a temporary file.

    Arguments:
        ext: Optional extension to give to the file.
        num: Optional number suffix.

    Returns:
        Name for a temporary file.
    """
    bn = base64.b64encode(os.urandom(12), b"__").decode()
    if num is not None and num > 0:
        bn += f"-{num:03d}"
    if ext:
        if not ext.startswith("."):
            ext = "." + ext
        bn += ext
    return bn


if __name__ == "__main__":  # Test {{{1
    print(tempname())
    print(tempname("foo"))
