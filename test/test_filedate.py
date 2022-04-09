# file: test_filedate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:06:50 +0200
# Last modified: 2022-04-09T16:54:43+0200
#

"""Tests for the filedate module."""

from filedate import fcdate, iso8601


def test_filedate():
    rv = fcdate("nameddict.py")
    assert iso8601(rv) == "2018-07-08T11:36:25+0200"
    rv = fcdate("nonexistant")
    assert rv is None
