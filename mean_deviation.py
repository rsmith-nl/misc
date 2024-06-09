# file: mean_deviation.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-04-21T19:07:27+0200
# Last modified: 2024-06-09T17:51:08+0200
"""
Calculate the mean deviation of samples.

This number is independent of the distribution.
"""

import statistics as stat


def amd(data):
    """
    Calculate the absolute mean deviation of a sequence of numbers.
    This calculates the mean of the sequence. Then all distances to the mean.
    It returns the mean of those distances

    Arguments:
        data: A sequence of numbers.

    Returns:
        The absolute mean deviation.

    Examples:
    >>> from mean_deviation import amd
    >>> amd([13,6,12,10,11,9,10,8,12,9])
    1.6
    """
    m = stat.mean(data)
    diff = [abs(n - m) for n in data]
    return stat.mean(diff)
