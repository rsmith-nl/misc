# file: rawbytes.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-04-21T18:38:09+0200
# Last modified: 2018-04-21T18:39:44+0200

from struct import pack


def rawbytes(s):
    """
    Convert a string to raw bytes without encoding

    Arguments:
        s (str): String to convert

    Return:
        The input string as bytes.
    """
    outlist = []
    for cp in s:
        num = ord(cp)
        if num < 255:
            outlist.append(pack('b', num))
        elif num < 65535:
            outlist.append(pack('>H', num))
        else:
            b = (num & 0xFF0000) >> 16
            H = num & 0xFFFF
            outlist.append(pack('>bH', b, H))
    return b''.join(outlist)
