#!/usr/bin/env python3
# file: filedate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-12-17 23:30:49 +0100
# Last modified: 2015-09-05 14:23:14 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to filedate.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from os import stat
from datetime import datetime
from pytz import timezone

_here = timezone('Europe/Amsterdam')


def fcdate(name):
    """Get the creation date of a file formatted as a string.

    :param name: name of the file to query
    :returns: @todo
    """
    try:
        bt = datetime.fromtimestamp(stat(name).st_birthtime, _here)
    except OSError:
        bt = datetime.now(_here)
    rv = bt.strftime('%F %T %z')
    return rv

# Tests
if __name__ == '__main__':
    for fn in ['functest.c', 'nonexistent']:
        print(fn, fcdate(fn))
