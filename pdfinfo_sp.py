# file: pdfinfo.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017-2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-09-10T16:53:54+0200
# Last modified: 2019-02-26T18:56:11+0100
"""Retrieve info dictionary from a PDF file."""

import subprocess as sp

__version__ = "2019.02.26"


def pdfinfo(path):  # {{{1
    """
    Retrieves the contents of the ‘info’ dictionary from a PDF file using
    the ``pdfinfo`` program.

    Arguments:
        path (str): The path to the PDF file to use.

    Returns:
        A dict containing the info dictionary, with the keys transformed to lower case.
    """
    rv = sp.run(["pdfinfo", path], stdout=sp.PIPE, stderr=sp.DEVNULL)
    if rv.returncode != 0:
        return {}
    pairs = {
        k.lower(): v.strip()
        for k, v in [ln.split(":", 1) for ln in rv.stdout.decode("utf-8").splitlines()]
    }
    return pairs
