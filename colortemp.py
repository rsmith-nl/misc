# file: colortemp.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-12-31T14:19:06+0100
# Last modified: 2018-04-21T18:47:18+0200
"""
Convert r,b,g values to a color temperature.

Based on the code in https://github.com/adafruit/Adafruit_TCS34725/blob/master/Adafruit_TCS34725.cpp
"""


def cct(r, g, b):
    """Convert 8-bit RGB color to a correlated color temperature.

    Arguments:
        r: Red value in the range 0-255.
        g: Green value in the range 0-255.
        b: Blue value in the range 0-255.

    Returns:
        Color temperature in Kelvin.
    """
    for v in (r, g, b):
        if v < 0 or v > 255:
            raise ValueError('color value out of range (0-255)')
    # Map rgb to XYZ. Note that the constants are multiplied by 257,
    # to map 2**8-1 to 2**16-1.
    X = (-36.70474 * r) + (398.15468 * g) + (-245.79737 * b)
    Y = (-83.43762 * r) + (405.64109 * g) + (-188.10087 * b)
    Z = (-175.27914 * r) + (198.07761 * g) + (144.77324 * b)
    # Calculate chromaticity coordinates.
    xc = X / (X + Y + Z)
    yc = Y / (X + Y + Z)
    # Use McCanny's formula
    n = (xc - 0.3320) / (0.1858 - yc)
    # Calculate final CCT.
    rv = (449.0 * n**3) + (3525.0 * n**2) + (6823.3 * n) + 5520.33
    return int(round(rv))


def lux(r, g, b):
    """Convert 8-bit RGB color to Lux.

    Arguments:
        r: Red value in the range 0-255.
        g: Green value in the range 0-255.
        b: Blue value in the range 0-255.

    Returns:
        Illuminance in Lux.
    """
    # Again, the constants are multiplied by 257.
    illuminance = (-83.43762 * r) + (405.64109 * g) + (-188.10087 * b)
    return abs(round(illuminance))
