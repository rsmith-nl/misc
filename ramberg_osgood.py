# file: ramberg_osgood.py
# vim:fileencoding=utf-8:ft=python
#
# Copyright © 2024 R.F. Smith <rsmith@xs4all.nl>
# SPDX-License-Identifier: MIT
# Created: 2024-05-27T21:19:29+0200
# Last modified: 2024-05-27T21:39:03+0200

import math
import os


def calculix_plastic(Rp, Rm, em, steps=6):
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

    Returns:
        A string containing the *PLASTIC data.
    """
    n = math.log(Rm/Rp)/math.log(em/0.002)
    H = Rp/(0.002**n)
    rng = Rm - Rp
    iv = rng/steps
    rv = ["*PLASTIC"]
    for j in range(steps+1):
        s = Rp + j * iv
        rv.append(f"{s:g},{round((s/H)**(1/n), 5)},293")
    return os.linesep.join(rv) + os.linesep
