# file: nameddict.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2015 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-04-10T08:47:11+0200
# Last modified: 2024-06-09T17:26:33+0200


class NamedDict(dict):
    """
    Dictionary subclass where attributes can be accessed with a dot.

    Examples:
    >>> from nameddict import NamedDict
    >>> t1 = NamedDict(x=1, y=2)
    >>> t1
    {'x': 1, 'y': 2}
    >>> t1.x
    1
    >>> t1.y
    2
    """

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
