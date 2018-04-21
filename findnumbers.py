# file: findnumbers.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-04-21T18:57:47+0200
# Last modified: 2018-04-21T19:02:58+0200
"""Extract numbers from a line."""


def findnumbers(line):
    items = line.split()
    numbers = []
    remain = []
    for it in items:
        try:
            numbers.append(float(it))
        except ValueError:
            remain.append(it)
    return numbers, remain
