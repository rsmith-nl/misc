# file: scan.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2019-03-07T10:06:18+0100
# Last modified: 2019-03-07T10:12:51+0100


def px2mm(pixels, resolution=1600, precision=2):
    """Convert scanned pixels to millimeters.

    Arguments:
        pixels: measurement in pixels.
        resolution: image resolution in pixels/inch.
        precision: number of significant digits for rounding.

    Returns:
        The converted measurement.
    """
    return round(25.4*pixels/resolution, precision)
