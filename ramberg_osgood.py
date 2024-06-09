# file: ramberg_osgood.py
# vim:fileencoding=utf-8:ft=python
#
# Copyright © 2024 R.F. Smith <rsmith@xs4all.nl>
# SPDX-License-Identifier: MIT
# Created: 2024-05-27T21:19:29+0200
# Last modified: 2024-06-09T08:22:29+0200

import math
import os


def calculix_plastic(Rp, Rm, em, steps=6, temp=293):
    """
    Calculate *PLASTIC properties for CalculiX.
    The calculation is basicall unit agnostic.
    However, Rp and Rm should be given in the same units and em should not be
    a percentage.

    Parameters:
        Rp: yield stress
        Rm: failure stress
        em: failure strain (dimensionless)
        steps: number of steps in the table
        temp: temperature for which the properties are valid

    Returns:
        A string containing the *PLASTIC data.

    Examples:
    >>> from ramberg_osgood import calculix_plastic
    >>> print(calculix_plastic(235, 435, 0.26, steps=5))
    *PLASTIC
    235,0.002,293
    275,0.00693,293
    315,0.02027,293
    355,0.05215,293
    395,0.12129,293
    435,0.26,293
    >>> print(calculix_plastic(850, 960, 0.1, steps=4))
    *PLASTIC
    850,0.002,293
    877.5,0.00557,293
    905,0.01501,293
    932.5,0.03929,293
    960,0.1,293
    """
    n = math.log(Rm/Rp)/math.log(em/0.002)
    H = Rp/(0.002**n)
    rng = Rm - Rp
    iv = rng/steps
    rv = ["*PLASTIC"]
    for j in range(steps+1):
        s = Rp + j * iv
        rv.append(f"{s:g},{round((s/H)**(1/n), 5)},{temp}")
    return os.linesep.join(rv) + os.linesep
