# file: test_htmlcolor.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-08 00:07:58 +0200
# Last modified: 2015-09-08 00:15:58 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to test_htmlcolor.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the htmlcolor module.

Run this test only with nosetests-3.4 -v test_htmlcolor.py
Run all tests with: nosetests-3.4 -v test_*
"""

from htmlcolor import rgb2html
from nose.tools import raises


def test_rgb():
    assert rgb2html(0, 0, 0) == '#000000'
    assert rgb2html(1.0, 0, 0) == '#ff0000'
    assert rgb2html(1.0, 1.0, 0) == '#ffff00'
    assert rgb2html(1.0, 1.0, 1.0) == '#ffffff'
    assert rgb2html(255, 255, 255) == '#ffffff'


@raises(ValueError)
def test_illegal_values():
    rgb2html(12, 234, 'a')
