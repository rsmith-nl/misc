# file: nameddict.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014-2015 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-04-10T08:47:11+0200
# Last modified: 2018-04-17T19:53:41+0200
"""Dictionary subclass where you can access attributes with a dot."""


class NamedDict(dict):

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
