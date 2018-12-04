# file: humidity.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-05-07T22:12:36+0200
# Last modified: 2018-05-07T22:15:58+0200

from math import exp


def absolute(T, rh):
    """Returns the absolute humidity in g/m³. This uses the formula found at
    https://carnotcycle.wordpress.com/2012/08/04/how-to-convert-relative-humidity-to-absolute-humidity/

    Parameters:
        T (float): Temperature in °C.
        rh (float): Relative humidity in %.
    """
    return 6.112 * exp(16.67 * T / (T + 243.5)) * rh * 2.1674 / (273.15 + T)
