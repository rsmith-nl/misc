# file: text_xpand.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-13 12:13:31 +0200
# Last modified: 2015-09-13 12:19:23 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to text_xpand.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Tests for the xpand module.

Run this test only with nosetests-3.4 -v text_xpand.py
Run all tests with: nosetests-3.4 -v test_*
"""

from xpand import xpand


def test_xpand():
    assert xpand('../h*') == ['../htmlcolor.py', '../hertz.py']
    assert xpand('foo') == ['foo']
    assert xpand([]) == []
    assert xpand('') == ['']
    assert xpand(['']) == ['']
