# file: test_htmlcolor.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-08 00:07:58 +0200
# Last modified: 2016-06-10 00:05:06 +0200
#

"""Tests for the htmlcolor module."""

from htmlcolor import rgb2html
import pytest


def test_rgb():
    assert rgb2html(0, 0, 0) == "#000000"
    assert rgb2html(1.0, 0, 0) == "#ff0000"
    assert rgb2html(1.0, 1.0, 0) == "#ffff00"
    assert rgb2html(1.0, 1.0, 1.0) == "#ffffff"
    assert rgb2html(255, 255, 255) == "#ffffff"


def test_illegal_values():
    with pytest.raises(ValueError):
        rgb2html(12, 234, "a")
