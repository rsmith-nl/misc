# file: postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-08-03 12:56:45 +0200
# Last modified: 2016-06-12 08:32:15 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

import operator
import math

_add, _sub, _mul = operator.add, operator.sub, operator.mul
_truediv, _pow, _sqrt = operator.truediv, operator.pow, math.sqrt
_sin, _cos, _tan, _radians = math.sin, math.cos, math.tan, math.radians
_asin, _acos, _atan = math.asin, math.acos, math.atan
_degrees, _log, _log10 = math.degrees, math.log, math.log10
_e, _pi = math.e, math.pi
_ops = {'+': (2, _add), '-': (2, _sub), '*': (2, _mul), '/': (2, _truediv),
        '**': (2, _pow), 'sin': (1, _sin), 'cos': (1, _cos), 'tan': (1, _tan),
        'asin': (1, _asin), 'acos': (1, _acos), 'atan': (1, _atan),
        'sqrt': (1, _sqrt), 'rad': (1, _radians), 'deg': (1, _degrees),
        'ln': (1, _log), 'log': (1, _log10)}
_okeys = tuple(_ops.keys())
_consts = {'e': _e, 'pi': _pi}
_ckeys = tuple(_consts.keys())


def postfix(expression):
    """
    Evaluate a postfix expression.

    Arguments:
        expression: The expression to evaluate. Should be a string or a
                    sequence of strings. In a string numbers and operators
                    should be separated by whitespace

    Returns:
        The result of the expression.
    """
    if isinstance(expression, str):
        expression = expression.split()
    stack = []
    for val in expression:
        if val in _okeys:
            n, op = _ops[val]
            if n > len(stack):
                raise ValueError('not enough data on the stack')
            args = stack[-n:]
            stack[-n:] = [op(*args)]
        elif val in _ckeys:
            stack.append(_consts[val])
        else:
            stack.append(float(val))
    return stack[-1]
