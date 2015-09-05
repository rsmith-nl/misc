# file: filedate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-12-17 23:30:49 +0100
# Last modified: 2015-09-05 15:11:55 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to filedate.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from os import stat
from datetime import datetime
from pytz import timezone

_here = timezone('Europe/Amsterdam')


def fcdate(name, tz=_here):
    """Get the creation date of a file formatted as a string.

    Arguments
        name: Name of the file to query.
        tz: Local timezone. Defaults to Europe/Amsterdam

    Returns:
        String containing the formatted date or None.
    """
    if isinstance(tz, str):
        tz = timezone(tz)
    try:
        bt = datetime.fromtimestamp(stat(name).st_birthtime, tz)
        rv = bt.strftime('%F %T %z')
    except OSError:
        rv = None
    return rv

# Tests
if __name__ == '__main__':
    for fn in ['nameddict.py', 'nonexistent']:
        print(fn, fcdate(fn))
