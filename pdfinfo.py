# file: pdfinfo.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2017-09-10 16:53:54 +0200
# Last modified: 2017-09-11 02:41:40 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to pdfinfo.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/
"""Retrieve info dictionary from a PDF file."""

from datetime import datetime as dt
import subprocess as sp
import re

__version__ = '1.0.0'


def pdfinfo(path):  # {{{1
    """Retrieves the Info dictionary from a PDF file.

    The information is converted to a Python dictionary.
    The values are converted to a suitable format.

    Arguments:
        path: String that indicates the location of the PDF file.

    Returns:
        A Python dictionary containing the file's info.
    """
    # Extract the info from a PDF file.
    text = sp.check_output(['pdfinfo', path]).decode('utf-8')
    # Convert info to a doctionary.
    info = dict(re.findall('(.*)?:\s+(.*)?\s+', text, re.MULTILINE))
    # Convert dates to datetime objects.
    keys = info.keys()
    for key in keys & ('CreationDate', 'ModDate'):
        info[key] = dt.strptime(info[key], '%c %Z')
    # Convert suitable values to integers
    for key in keys & ('File size', 'Pages', 'Page rot'):
        info[key] = int(info[key].split()[0])
    # Convert quitable values to boolean
    for key in keys & ('Encrypted', 'JavaScript', 'Optimized', 'Suspects',
                       'Tagged'):
        info[key] = info[key].split()[0] in ("yes", "true", "t", "1")
    return info
