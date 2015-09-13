# file: postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-08-03 12:56:45 +0200
# Last modified: 2015-09-13 06:46:42 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from operator import add, sub, mul, truediv, pow
from math import (sin, cos, tan, asin, acos, atan, sqrt, radians, degrees, log,
                  log10, pi, e)

_binops = {'+': add, '-': sub, '*': mul, '/': truediv, '**': pow}
_binopr = tuple(_binops.keys())
_unops = {'sin': sin, 'cos': cos, 'tan': tan, 'asin': asin, 'acos': acos,
          'atan': atan, 'sqrt': sqrt, 'rad': radians, 'deg': degrees, 'ln':
          log, 'log': log10}
_unopr = tuple(_unops.keys())
_consts = {'e': e, 'pi': pi}
_constk = tuple(_consts.keys())


def postfix(expr):
    """Evaluate a postfix expression.
    Numbers and operators should be separated by whitespace.

    Arguments:
        expr: The expression to evaluate.

    Returns:
        The result of the expression.
    """
    items = expr.split()
    if not items:
        raise ValueError("Empty expression")
    stk = []
    for i in items:
        if i in _binopr:
            try:
                b, a = stk.pop(), stk.pop()
                stk.append(_binops[i](a, b))
            except IndexError:
                raise ValueError('Invalid expression; empty stack')
            except KeyError:
                raise ValueError('Invalid operator')
        elif i in _unopr:
            a = stk.pop()
            stk.append(_unops[i](a))
        elif i in _constk:
            stk.append(_consts[i])
        else:
            stk.append(float(i))
    return stk[-1]
