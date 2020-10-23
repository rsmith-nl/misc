# file: dround.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>
# Created: 2019-05-22T22:55:03+0200
# Last modified: 2019-05-22T23:51:47+0200
"""Use the decimal module to round floating point numbers in a reasonable way.

>>> dround(0.999999)
1.0
>>> dround(0.006599)
0.0066
>>> dround(0.0749999)
0.075
"""

from decimal import Decimal


def dround(num):
    dec = Decimal(num)
    adj = abs(dec.adjusted()) + 1
    return round(num, adj)
