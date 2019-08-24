# file: regression.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2019-08-03T18:47:27+0200
# Last modified: 2019-08-24T23:39:03+0200
"""Linear regression.

Inspired by: http://www.codedrome.com/linear-regression-in-python/
"""


import statistics as stat


def linear(x, y):
    """
    Calculates the linear regression between two sequences of data.

    Arguments:
        x (sequence): independent data.
        y (sequence): dependant data.

    Returns:
        the coefficients of y = a·x + b.

    Examples:
    >>> x = (10, 20, 40, 45, 60, 65, 75, 80)
    >>> y = (32, 44, 68, 74, 92, 98, 110, 116)
    >>> linea(x, y)
    (1.2, 20.0)
    >>> y = [40, 40, 60, 80, 90, 110, 100, 130]
    >>> linear(x, y)
    (1.2424877707896576, 19.902166317260658)
    >>> y = [100, 10, 130, 90, 40, 80, 180, 50]
    >>> linear(x, y)
    (0.4416491963661775, 63.19357092941999)
    """
    if len(x) != len(y):
        raise ValueError('y data and x data should have the same size')
    x_mean = stat.mean(x)
    y_mean = stat.mean(y)
    prod_mean = sum(i*j for i, j in zip(x, y))/len(x)
    x_var = stat.pvariance(x)
    a = (prod_mean - (x_mean * y_mean)) / x_var
    b = y_mean - a * x_mean
    return a, b
