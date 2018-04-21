# file: frange.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2016-2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2016-01-08T07:21:12+0100
# Last modified: 2018-04-21T18:52:29+0200


def frange(x, y, jump):  # {{{1
    while x < y:
        yield x
        x += jump


def frangeeq(x, y, jump):  # {{{1
    while x <= y:
        yield x
        x += jump
