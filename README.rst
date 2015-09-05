Miscellaneous modules
#####################

:date: 2015-09-05
:author: Roland Smith

.. Last modified: 2015-09-05 17:23:23 +0200

Introduction
============

This is a collection of small utilities that are not big enough to warrant
a separate repository.


Contents
========

erase.py
--------

Script to erase a file by overwriting it with zeroes. The file is renamed to
a random base64 encoded name and then deleted.

filedate.py
-----------

The ``fcdate`` function returns the creation date of a file as a string.

hertz.py
--------

Calculates Hertz contact stresses.

htmlcolor.py
------------

The function ``rgb2html`` converts an RGB color into a HTML color reference.

nameddict.py
------------

The ``NamedDict`` class is a subclass of a ``dict`` that allows you to access
dict values as attributes by “dot-notation”;

.. code-block:: python

    In [4]: d = NamedDict()

    In [5]: d.a = 1

    In [6]: d.b = 2

    In [7]: d
    Out[7]: {'a': 1, 'b': 2}

    In [8]: d['a']
    Out[8]: 1

postfix.py
----------

The ``postfix`` function evaluates postfix expressions.

tempname.py
-----------

The ``tempname`` function creates a name for a temporary file.

xpand.py
--------

The function ``xpand`` uses the ``glob`` module to provide filename expansions
for operating systems incapable of doing so.
