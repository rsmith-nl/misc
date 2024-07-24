# file: services.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2015 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2015-09-05T19:01:04+0200
# Last modified: 2024-06-09T17:56:07+0200

import re


def services(filename="/etc/services"):  # {{{1
    """
    Generate a dictionary of the available services from the services file,
    by default /etc/services.

    Arguments:
        filename: Name of the services file.

    Returns:
        A dict in the form of {25: 'smtp', 80: 'http', ...}

    Examples:
    >>> from services import services
    >>> localservices = services()
    >>> localservices[25]
    'smtp'
    >>> localservices[80]
    'http'
    """
    with open(filename) as serv:
        data = serv.read()
    matches = re.findall("\n" + r"(\S+)\s+(\d+)/", data)
    return {int(num): name for name, num in set(matches)}
