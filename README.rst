Miscellaneous modules
#####################

:date: 2015-09-05
:author: Roland Smith

.. Last modified: 2017-09-11 03:00:49 +0200

Introduction
============

This is a collection of small utilities that are not big enough to warrant
a separate repository.

The subdirectory ``tests`` contains tests for this code. Running the tests
requires nose_.

.. _nose: https://nose.readthedocs.org/en/latest/


Contents
========


filedate.py
-----------

The ``fcdate`` function returns the creation date of a file as a string.


group
-----

The ``subgroup`` function split an iterat up into a list of sub-iterators.


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


pdfinfo
-------

The ``pdfinfo`` function extracts the Info Dictionary from a PDF file.


postfix.py
----------

The ``postfix`` function evaluates postfix expressions.


services
--------

The ``services`` function returns a dict describing the defined services,
indexed by port number.


tempname.py
-----------

The ``tempname`` function creates a name for a temporary file.


xpand.py
--------

The function ``xpand`` uses the ``glob`` module to provide filename expansions
for operating systems incapable of doing so.
