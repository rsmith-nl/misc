# file: test_filedate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:06:50 +0200
# Last modified: 2018-07-08T11:44:57+0200
#

"""Tests for the filedate module."""

from filedate import fcdate, iso8601


def test_filedate():
    rv = fcdate("nameddict.py")
    assert iso8601(rv) == "2015-04-10T08:47:11+0200"
    rv = fcdate("nonexistant")
    assert rv is None
