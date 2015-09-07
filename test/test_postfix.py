# file: test_postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-07 23:17:26 +0200
# Last modified: 2015-09-07 23:35:52 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to test_postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the postfix module.

Run this test only with nosetests-3.4 -v test_postfix.py
Run all tests with: nosetests-3.4 -v test_*
"""

from postfix import postfix
from nose.tools import raises


def test_addition():
    assert postfix('1 7 +') == 8


def test_substraction():
    assert postfix('7 3 -') == 4


def test_multiplication():
    assert postfix('7 3 *') == 21


def test_division():
    assert postfix('48 8 /') == 6


def test_pow():
    assert postfix('2 3 **') == 8


def test_multiple():
    assert postfix('48 8 / 3 + 7 *') == 63


@raises(ValueError)
def test_emptyexpr():
    postfix('')


@raises(ValueError)
def test_emptystack():
    postfix('1 2 + /')
