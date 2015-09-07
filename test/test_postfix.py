# file: test_postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-07 23:17:26 +0200
# Last modified: 2015-09-08 00:03:00 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to test_postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the postfix module.

Run this test only with nosetests-3.4 -v test_postfix.py
Run all tests with: nosetests-3.4 -v test_*
"""

from math import pi
from postfix import postfix
from nose.tools import raises


def test_binops():
    assert postfix('1 7 +') == 8
    assert postfix('7 3 -') == 4
    assert postfix('7 3 *') == 21
    assert postfix('48 8 /') == 6
    assert postfix('2 3 **') == 8


def test_unops():
    assert postfix('pi deg') == 180
    assert postfix('4 sqrt') == 2
    assert postfix('90 rad 2 *') == pi
    assert postfix('100 log') == 2


def test_trig():
    assert postfix('pi cos') == -1
    assert postfix('pi 2 / sin') == 1
    assert 0.99 < postfix('pi 4 / tan') < 1.01


def test_multiple():
    assert postfix('48 8 / 3 + 7 *') == 63


@raises(ValueError)
def test_emptyexpr():
    postfix('')


@raises(ValueError)
def test_emptystack():
    postfix('1 2 + /')
