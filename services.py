# file: services.py
# vim:fileencoding=utf-8:ft=python:fdm=marker
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-09-05 19:01:04 +0200
# Last modified: 2017-09-11 02:48:37 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to services.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

import re


def services(filename='/etc/services'):  # {{{1
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
    matches = re.findall('\n(\S+)\s+(\d+)/', data)
    return {int(num): name for name, num in set(matches)}
