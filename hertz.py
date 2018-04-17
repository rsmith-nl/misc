# file: hertz.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2015 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-05-20T19:09:51+0200
# Last modified: 2018-04-17T20:49:55+0200
import math


def cylinder_cylinder(F, L, D1, D2, E1, E2):
    """
    Calculate line contact pressure between two cylinders.

    Arguments;
        F: Force, e.g. in [N].
        L: Contact length, e.g. in [mm].
        D1: Diameter of first cylinder in e.g. [mm].
        D2: Diameter of second cylinder in e.g. [mm].
        E1: Young's modulus of the first cylinder in e.g. [MPa].
        E2: Young's modulus of the second cylinder in e.g. [MPa].

    Returns:
        Maximum contact pressure, e.g. in [MPa]
    """
    A = F/(2.86*L)
    B = (D1 + D2)/(D1*D2)
    C = 2*E1*E2/(E1 + E2)
    Pmax = math.sqrt(A*B*C)
    return Pmax


def cylinder_plane(F, L, D1, E1, E2):
    """
    Calculate line contact pressure a cylinder and a plane.

    Arguments;
        F: Force, e.g. in [N].
        L: Contact length, e.g. in [mm].
        D1: Diameter of cylinder in e.g. [mm].
        E1: Young's modulus of first cylinder in e.g. [MPa].
        E2: Young's modulus of the plane in e.g. [MPa].

    Returns:
        Maximum contact pressure, e.g. in [MPa]
    """
    A = F/(2.86*L)
    B = 1/D1
    C = 2*E1*E2/(E1 + E2)
    Pmax = math.sqrt(A*B*C)
    return Pmax
