# file: mean_deviation.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-04-21T19:07:27+0200
# Last modified: 2018-04-21T19:09:41+0200
"""
Calculate the mean deviation of samples.

See http://www.leeds.ac.uk/educol/documents/00003759.htm

This number is independent of the distribution.
"""

import numpy as np
import statistics as stat


def np_amd(arr):
    """
    Calculate the absolute mean deviation of an array of numbers.
    Starting from an array, we calculate the mean, and then take the absolute
    value of the difference between the array and its mean.
    We then calculate and return the mean value of this difference.

    Arguments:
        arr (ndarray): input array

    Returns:
        The absolute mean deviation.
    """
    return np.mean(np.abs(arr - np.mean(arr)))


def amd(data):
    """
    Calculate the absolute mean deviation.

    Arguments:
        data: A sequence of numbers.

    Returns:
        The absolute mean deviation.
    """
    m = stat.mean(data)
    diff = [abs(n - m) for n in data]
    return stat.mean(diff)
