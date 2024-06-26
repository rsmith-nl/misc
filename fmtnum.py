# file: fmtnum.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2016 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2016-05-23T23:12:24+0200
# Last modified: 2024-06-09T09:27:12+0200
"""Format numbers with metric prefixes."""

import math


def fmtnum(num, unit=""):
    """Formats a number with numeric prefix.

    Arguments:
        num: Number to be formatted.
        unit: String containing the SI unit to be used for the number.

    Returns:
        A string containing the formatted number.

    Examples:
    >>> from fmtnum import fmtnum
    >>> fmtnum(1.382e7, "Pa")
    '13.82 MPa'
    >>> fmtnum(3527, "g")
    '3.527 kg'
    >>> fmtnum(3.527, "kg")
    '3.527'
    """
    d = (10, "d")
    h = (1e2, "h")
    k = (1e3, "k")
    M = (1e6, "M")
    G = (1e9, "G")
    T = (1e12, "T")
    P = (1e15, "P")
    E = (1e18, "E")
    table = {
        1: d,
        2: h,
        3: k,
        4: k,
        5: k,
        6: M,
        7: M,
        8: M,
        9: G,
        10: G,
        11: G,
        12: T,
        13: T,
        14: T,
        15: P,
        16: P,
        17: P,
        18: E,
    }
    num = float(num)
    exp = math.log10(num)
    if num < 0:
        exp = int(exp) - 1
    else:
        exp = int(exp)
    try:
        denum, suffix = table[exp]
        val = num / denum
        return f"{val:g} {suffix}{unit}"
    except KeyError:
        return f"{num:g}"
