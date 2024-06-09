# file: postfix.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2014 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2014-12-07T13:30:14+0100
# Last modified: 2024-06-09T08:31:33+0200

import operator
import math

# Global constants {{{1
_add, _sub, _mul = operator.add, operator.sub, operator.mul
_truediv, _pow, _sqrt = operator.truediv, operator.pow, math.sqrt
_sin, _cos, _tan, _radians = math.sin, math.cos, math.tan, math.radians
_asin, _acos, _atan = math.asin, math.acos, math.atan
_degrees, _log, _log10 = math.degrees, math.log, math.log10
_e, _pi = math.e, math.pi
_ops = {
    "+": (2, _add),
    "-": (2, _sub),
    "*": (2, _mul),
    "/": (2, _truediv),
    "**": (2, _pow),
    "sin": (1, _sin),
    "cos": (1, _cos),
    "tan": (1, _tan),
    "asin": (1, _asin),
    "acos": (1, _acos),
    "atan": (1, _atan),
    "sqrt": (1, _sqrt),
    "rad": (1, _radians),
    "deg": (1, _degrees),
    "ln": (1, _log),
    "log": (1, _log10),
}
_okeys = tuple(_ops.keys())
_consts = {"e": _e, "pi": _pi}
_ckeys = tuple(_consts.keys())


def postfix(expression):  # {{{1
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
                raise ValueError("not enough data on the stack")
            args = stack[-n:]
            stack[-n:] = [op(*args)]
        elif val in _ckeys:
            stack.append(_consts[val])
        else:
            stack.append(float(val))
    return stack[-1]
