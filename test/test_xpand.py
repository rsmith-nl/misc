# file: text_xpand.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:13:31 +0200
# Last modified: 2018-07-08T11:47:26+0200
#

"""Tests for the xpand module."""

from xpand import xpand


def test_xpand():
    rv = xpand("h*")
    assert rv == ["htmlcolor.py", "hertz.py", "humidity.py"]
    rv = xpand("foo")
    assert rv == ["foo"]
    rv = xpand([])
    assert xpand([]) == []
    rv = xpand("")
    assert rv == [""]
    rv = xpand([""])
    assert rv == [""]
