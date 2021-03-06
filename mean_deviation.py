# file: mean_deviation.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-04-21T19:07:27+0200
# Last modified: 2019-07-13T10:16:34+0200
"""
Calculate the mean deviation of samples.

See http://www.leeds.ac.uk/educol/documents/00003759.htm

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
    """
    m = stat.mean(data)
    diff = [abs(n - m) for n in data]
    return stat.mean(diff)
