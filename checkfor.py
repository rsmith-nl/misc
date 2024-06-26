# file: checkfor.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2012 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2012-12-13T01:39:03+01:00
# Last modified: 2024-06-09T08:29:24+0200

import logging
import subprocess as sp
import sys

"""
Note: I don't use this much anymore. The simpler solution is:

progs = ['gs', 'gnuplot', 'pkg']
try:
    for p in progs:
        sp.run([p], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
except FileNotFoundError:
    logging.error(f'required program “{p}” not found')
    sys.exit(1)
"""


def checkfor(args, rv=0):
    """
    Ensure that a program necessary for using this script is available.

    If the required utility is not found, this function will exit the program.

    Arguments:
        args: String or list of strings of commands. A single string may not
            contain spaces.
        rv: Expected return value from evoking the command.
    """
    if isinstance(args, str):
        if " " in args:
            raise ValueError("no spaces in single command allowed")
        args = [args]
    else:
        if not isinstance(args, (list, tuple)):
            raise ValueError("args should be a list or tuple")
        if not all(isinstance(x, str) for x in args):
            raise ValueError("args should be a list or tuple of strings")
    try:
        cp = sp.run(args)
    except FileNotFoundError as oops:
        logging.error(f'required program "{args[0]}" not found: {oops.strerror}.')
        sys.exit(1)
    if cp.returncode != rv:
        logging.error(f"returncode {cp.returncode} should be {rv}")
        sys.exit(1)
    logging.info(f'found required program "{args[0]}"')
