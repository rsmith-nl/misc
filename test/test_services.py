# file: test_services.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-08 22:19:05 +0200
# Last modified: 2016-06-10 00:09:47 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to test_services.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the services module."""

from services import services


def test_services():
    service = services()
    assert service is not None
    assert service[22] == 'ssh'
    assert service[70] == 'gopher'
    assert service[80] == 'http'
    assert service[53] == 'domain'
    assert service[389] == 'ldap'
    assert service[443] == 'https'
    assert service[873] == 'rsync'
    assert service[9418] == 'git'
