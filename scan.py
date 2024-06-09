# file: scan.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2019-03-07T10:06:18+0100
# Last modified: 2024-06-09T17:37:09+0200


def px2mm(pixels, resolution=1600, precision=2):
    """Convert scanned pixels to millimeters.

    Arguments:
        pixels: measurement in pixels.
        resolution: image resolution in pixels/inch.
        precision: number of significant digits for rounding.

    Returns:
        The converted measurement.

    Examples:
    >>> from scan import px2mm
    >>> px2mm(1600)
    25.4
    >>> px2mm(17)
    0.27
    """
    return round(25.4 * pixels / resolution, precision)
