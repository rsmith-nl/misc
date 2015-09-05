#!/usr/bin/env python3
# file: erase.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2012-10-06 20:11:22
# Last modified: 2015-09-05 14:19:31 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to erase.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from base64 import b64encode
# import logging
import sys
import os

_bufsize = 128*1024
_buf = b'\0' * _bufsize


def erase(f):
    """Overwrite a file with zeroes and remove it.

    Arguments:
        f: Name of the file to erase
    """
    path, fname = os.path.split(f)
    try:
        stat = os.stat(f)
    except FileNotFoundError:
        return
#    logging.debug('path = {}'.format(path))
#    logging.debug('fname = {}'.format(fname))
#    logging.debug('stat(fname) = {} bytes'.format(stat.st_size))
    rem = stat.st_size % _bufsize
#    logging.debug('rem = {}'.format(rem))
    cnt = int((stat.st_size - rem) / _bufsize)
#    logging.debug('cnt = {}'.format(cnt))
    with open(f, 'rb+') as of:
        for t in range(cnt):
            of.write(_buf)
        of.write(b'\0' * rem)
        of.flush()
#        logging.debug('file {} filled with zeroes'.format(fname))
    enc = b64encode(os.urandom(len(fname)), altchars=b'__')
    newname = enc[:len(fname)].decode('ascii')
    newf = os.path.join(path, newname)
    os.rename(f, newf)
#    logging.debug('{} renamed to {}'.format(fname, newf))
    os.remove(newf)
#    logging.debug('file {} removed'.format(fname))


def main(args):
    """Main program.

    :param args: command line arguments
    """
#    logging.basicConfig(level=logging.DEBUG)
#                        format='%(asctime)s %(levelname)s: %(message)s')
    if len(args) == 1:
        print("Usage: {} file ...".format(args[0]))
        sys.exit(0)
    for n in args[1:]:
        erase(n)

if __name__ == '__main__':
    main(sys.argv)
