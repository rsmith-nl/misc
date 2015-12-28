# file: nameddict.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-12-05 23:55:16 +0100
# Last modified: 2015-12-28 22:10:53 +0100
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to struct.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Dictionary subclass where you can access attributes with a dot."""


class NamedDict(dict):

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
