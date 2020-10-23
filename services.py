# file: services.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2015-2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-09-05T19:01:04+0200
# Last modified: 2018-04-17T20:44:27+0200

import re


def services(filename="/etc/services"):  # {{{1
    """
    Generate a dictionary of the available services from the services file,
    by default /etc/services.

    Arguments:
        filename: Name of the services file.

    Returns:
        A dict in the form of {25: 'smtp', 80: 'http', ...}
    """
    with open(filename) as serv:
        data = serv.read()
    matches = re.findall("\n(\S+)\s+(\d+)/", data)
    return {int(num): name for name, num in set(matches)}
