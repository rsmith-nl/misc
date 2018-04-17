# file: filedate.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014-2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-12-17T23:30:49+0100
# Last modified: 2018-04-17T20:47:32+0200

from datetime import datetime
import os
import subprocess as sp
from pytz import timezone

_here = timezone('Europe/Amsterdam')


def fcdate(name, tz=_here):
    """
    Get the creation date of a file formatted as a string.

    Arguments
        name: Name of the file to query.
        tz: Local timezone. Defaults to Europe/Amsterdam

    Returns:
        A datetime object.
    """
    if not os.path.exists(name):
        return None
    if isinstance(tz, str):
        tz = timezone(tz)
    try:
        rv = datetime.fromtimestamp(os.stat(name).st_birthtime, tz)
    except OSError:
        rv = None
    return rv


def gitdate(path, tz=_here):
    """
    If the file is in a directory under git control, get the date of
    the first git checkin, if available.

    Arguments:
        path (str): Path to the file to query
        tz: Local timezone. Defaults to Europe/Amsterdam

    Returns:
        A datetime object.
    """
    if not os.path.exists('.git'):
        return None
    if not os.path.exists(path):
        return None
    args = ['git', '--no-pager', 'log', '--format=%at', path]
    ts = int(sp.check_output(args).splitlines()[-1].decode('ascii'))
    date = datetime.fromtimestamp(ts, tz)
    return date


def iso8601(dt):
    if dt:
        return dt.strftime('%FT%T%z')
    else:
        return None


# Tests
if __name__ == '__main__':
    for fn in ['nameddict.py', 'nonexistent']:
        print(fn, '(file)', iso8601(fcdate(fn)))
        print(fn, '(git)', iso8601(gitdate(fn)))
