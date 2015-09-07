# file: postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-08-03 12:56:45 +0200
# Last modified: 2015-09-07 23:39:43 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from operator import add, sub, mul, truediv, pow

_binops = {'+': add, '-': sub, '*': mul, '/': truediv, '**': pow}
_binopr = tuple(_binops.keys())


def postfix(expr):
    """Evaluate a postfix expression.
    Numbers should be separated by spaces.

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
        else:
            stk.append(float(i))
    return stk[-1]
