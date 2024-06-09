# file: htmlcolor.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-04-01T22:23:24+0200
# Last modified: 2024-06-09T08:30:30+0200
"""Conversion routines for HTML colors."""


def rgb2html(r, g, b):  # {{{1
    """
    Converts an RGB color to a HTML color string.
    All the arguments are clamped to the appropriate range for their type.

    Arguments:
        r: Red value, integer (0--255) or float (0--1.0).
        g: Green value, idem.
        b: Blue value, idem.

    Returns:
        hexadecimal HTML color values string

    Exceptions:
        Raises a ValueError if any of the arguments is not an int or a float.
    """

    def chkarg(a):
        if isinstance(a, int):  # clamp to range 0--255
            if a < 0:
                a = 0
            elif a > 255:
                a = 255
        elif isinstance(a, float):  # clamp to range 0.0--1.0
            if a < 0.0:
                a = 0
            elif a > 1.0:
                a = 255
            else:
                a = int(round(a * 255))
        else:
            raise ValueError("Arguments must be integers or floats.")
        return a

    r = chkarg(r)
    g = chkarg(g)
    b = chkarg(b)
    return f"#{r:02x}{g:02x}{b:02x}"
