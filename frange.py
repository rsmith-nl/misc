# file: frange.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2016 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2016-01-08T07:21:12+0100
# Last modified: 2024-06-09T09:21:49+0200


def frange(start, stop, step=1.0):
    """
    Range for floating point numbers.

    Arguments:
        start: Value to start at.
        stop: The sequence stops when this value is reached or exceeded.
        step: Step for each iteration.

    Examples:
    >>> from frange import frange
    >>> list(frange(1, 3, 0.5))
    [1, 1.5, 2.0, 2.5]
    >>> list(frange(1, -3, 0.5))
    [1, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]
    """
    if stop > start:
        while start < stop:
            yield start
            start += step
    elif stop < start:
        if step > 0:
            step = -step
        while start > stop:
            yield start
            start += step


def frangele(start, stop, step=1.0):
    """
    Inclusive range for floating point numbers.

    Arguments:
        start: Value to start at.
        stop: The sequence stops when this value is exceeded.
        step: Step for each iteration.

    Examples:
    >>> from frange import frangele
    >>> list(frangele(1, 3, 0.5))
    [1, 1.5, 2.0, 2.5, 3.0]
    >>> list(frangele(1, -3, 0.5))
    [1, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0]
    """
    if stop > start:
        while start <= stop:
            yield start
            start += step
    elif stop < start:
        if step > 0:
            step = -step
        while start >= stop:
            yield start
            start += step
