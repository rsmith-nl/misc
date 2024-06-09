# file: filedate.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-12-17T23:30:49+0100
# Last modified: 2024-06-09T17:27:28+0200

from datetime import datetime
from dateutil.tz import gettz
import os
import subprocess as sp

# Get the local timezone.
_here = gettz()


def fcdate(name, tz=_here):
    """
    Get the creation date of a file.

    Arguments
        name: Name of the file to query.
        tz: Timezone. Defaults to the local timezone

    Returns:
        A datetime object.

    Examples:
    >>> from filedate import fcdate
    >>> fcdate("nameddict.py")
    datetime.datetime(2024, 6, 9, 17, 26, 33, 793181, tzinfo=tzfile('/etc/localtime'))
    """
    if not os.path.exists(name):
        return None
    if isinstance(tz, str):
        tz = gettz(tz)
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
        tz: Local timezone. Defaults to the local timezone.

    Returns:
        A datetime.datetime object.

    Examples:
    >>> from filedate import gitdate
    >>> gitdate("filedate.py")
    datetime.datetime(2015, 9, 5, 14, 29, 19, tzinfo=tzfile('/etc/localtime'))
    """
    if not os.path.exists(".git"):
        return None
    if not os.path.exists(path):
        return None
    args = ["git", "--no-pager", "log", "--format=%at", path]
    ts = int(sp.check_output(args).splitlines()[-1].decode("ascii"))
    date = datetime.fromtimestamp(ts, tz)
    return date


def iso8601(dt):
    """
    Converts a datetime object to an ISO 8601 formatted date string.

    Arguments:
        dt (datatime.datetime): Datetime to convert.

    Returns:
        The datetime object as an ISO 8601 formatted date string.

    Examples:
    >>> from filedate import gitdate, iso8601
    >>> iso8601(gitdate("filedate.py"))
    '2015-09-05T14:29:19+0200'
    """
    if dt:
        return dt.strftime("%FT%T%z")
    else:
        return None
