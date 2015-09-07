# file: htmlcolor.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-07-12 01:38:08 +0200
# Last modified: 2015-09-08 00:11:18 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to htmlcolor.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Conversion routines for HTML colors."""


def rgb2html(r, g, b):
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
                a = int(round(a*255))
        else:
            raise ValueError('Arguments must be integers or floats.')
        return a
    r = chkarg(r)
    g = chkarg(g)
    b = chkarg(b)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
