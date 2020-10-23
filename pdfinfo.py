# file: pdfinfo.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>
# Created: 2019-07-08T02:24:59+0200
# Last modified: 2019-07-08T19:19:06+0200
"""Module to retrieve information from a PDF file."""

import sys
import logging


def pdfinfo(path):
    lookups = (b"/Author", b"/Creator", b"/Producer", b"/CreationDate", b"/ModDate")
    logging.debug(f"reading {path}")
    with open(path, "rb") as f:
        data = f.read()
    # Find the trailer, and the Info reference in the trailer
    istart = data.find(b"\ntrailer") + 8
    istart = data.find(b"/Info", istart) + 6
    iend = data.find(b"R", istart) - 1
    # Extract the Info object number and generation
    objid = data[istart:iend].strip()
    logging.debug("Info object is " + objid.decode("ascii"))
    ostart = data.find(objid + b" obj")
    ostart = data.find(b"<<", ostart) + 3
    oend = data.find(b">>", ostart)
    # For now.
    # return data[ostart:oend]
    info = data[ostart:oend]
    locations = [
        (data.find(item), item.decode("ascii")) for item in lookups if item in info
    ]
    locations.sort(key=lambda i: i[0])
    logging.debug("found " + " ".join(t[1] for t in locations))
    return locations


# Run a test.
def _main(argv):
    """
    Entry point for pdfinfo.py.

    Arguments:
        argv: command line arguments
    """
    logging.basicConfig(level="DEBUG", format="%% %(levelname)s: %(message)s")
    for fn in argv:
        logging.info(pdfinfo(fn))
        print("-----------------------------------------")
        sys.stdout.flush()


if __name__ == "__main__":
    _main(sys.argv[1:])
