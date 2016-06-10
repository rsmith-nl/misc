# file: text_xpand.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:13:31 +0200
# Last modified: 2016-06-11 00:37:30 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to text_xpand.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the xpand module."""

from xpand import xpand


def test_xpand():
    rv = xpand('h*')
    assert rv == ['htmlcolor.py', 'hertz.py']
    rv = xpand('foo')
    assert rv == ['foo']
    rv = xpand([])
    assert xpand([]) == []
    rv = xpand('')
    assert rv == ['']
    rv = xpand([''])
    assert rv == ['']
