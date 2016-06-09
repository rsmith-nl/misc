# file: test_filedate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:06:50 +0200
# Last modified: 2016-06-10 00:03:29 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to test_filedate.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the filedate module."""

from filedate import fcdate


def test_filedate():
    rv = fcdate('nameddict.py')
    assert rv == '2015-04-10 08:47:11 +0200'
    rv = fcdate('nonexistant')
    assert rv is None
