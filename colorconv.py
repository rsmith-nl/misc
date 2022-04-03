# file: colorconv.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2022 R.F. Smith <rsmith@xs4all.nl>
# Created: 2022-04-03T11:07:12+0200
# Last modified: 2022-04-03T12:12:30+0200

def normalize(c, name):
    """
    Normalize a color to a floating point number between 0 and 1.

    Arguments:
        c (float or int): color value.
        name (str): name of the color to use in exceptions.

    Returns:
        Floating point color value in the range 0−1 inclusive.
    """
    if isinstance(c, float):
        if c < 0.0 or c > 1.0:
            raise(ValueError, f"float {name} color value “{c}” is out of bounds")
        return c
    elif isinstance(c, int):
        if c < 0 or c > 255:
            raise(ValueError, f"integer {name} color value “{c}” is out of bounds")
        return c/255.0
    else:
        raise(ValueError, f"{name} color value must be a float or integer")


def cmyk2rgb(c, m, y, k):
    """
    Convert CMYK colors to RGB. Handles both float and integer arguments.
    Internally it normalized colors to floating point representations.

    Arguments:
        c: cyan component
        m: magenta component
        y: yellow component
        k: black component.

    Returns:
        A 3-tuple (R, G, B) of floats in the range 0−1 inclusive.
    """
    c = normalize(c, "cyan")
    m = normalize(m, "magenta")
    y = normalize(y, "yellow")
    k = normalize(k, "black")
    r = (1-c)*(1-k)
    g = (1-m)*(1-k)
    b = (1-y)*(1-k)
    return r, g, b


def cmykstring2rgbstring(s):
    """
    Convert a string containing floating point CMYK to a string
    containing floating point RGB.
    """
    c, m, y, k = [float(j) for j in s.split()]
    r, g, b = cmyk2rgb(c, m, y, k)
    return f"{r:.6f} {g:.6f} {b:.6f}"
