Miscellaneous modules
#####################

:date: 2015-09-05
:author: Roland Smith

.. Last modified: 2017-09-16 23:50:53 +0200

Introduction
============

This is a collection of small utilities that are not big enough to warrant
a separate repository.

The subdirectory ``tests`` contains tests for this code. Running the tests
requires nose_ or pytest_.

.. _nose: https://nose.readthedocs.org/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/

Running the tests from the ``misc`` directory using ``tcsh`` done as follows.

.. code-block:: console

    # in tcsh
    env PYTHONPATH=. pytest-3.6 test/
    # in a POSIX shell
    PYTHONPATH=. pytest-3.6 test/

(Adjust the name for the ``pytest`` program according to your environment.)


Contents
========


filedate.py
-----------

The ``fcdate`` function returns the creation date of a file as a string.

.. code-block:: python

    In [2]: from filedate import fcdate

    In [3]: fcdate('README.rst')
    Out[3]: '2015-09-05 14:29:54 +0200'


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

.. code-block:: python

    In [1]: from postfix import postfix

    In [2]: postfix('3 2 ** 1 -')
    Out[2]: 8.0


services
--------

The ``services`` function returns a dict describing the defined services,
indexed by port number.

.. code-block:: python

    In [2]: from services import services

    In [3]: data = services()

    In [4]: data[80]
    Out[4]: 'http'

    In [5]: data[22]
    Out[5]: 'ssh'


tempname.py
-----------

The ``tempname`` function creates a name for a temporary file.


xpand.py
--------

The function ``xpand`` uses the ``glob`` module to provide filename expansions
for operating systems incapable of doing so.
