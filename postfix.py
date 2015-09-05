# file: postfix.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-08-03 12:56:45 +0200
# Last modified: 2015-09-05 14:23:27 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to postfix.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from operator import add, sub, mul, truediv

_ops = {'+': add, '-': sub, '*': mul, '/': truediv}
_opchars = ''.join(_ops.keys())


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
        if i not in _opchars:
            stk.append(float(i))
        else:
            try:
                b, a = stk.pop(), stk.pop()
                stk.append(_ops[i](a, b))
            except IndexError:
                raise ValueError('Invalid expression; empty stack')
            except KeyError:
                raise ValueError('Invalid operator')
    return stk[-1]


def test():
    allexpr = ['1 2 +', '1 2 -', '1 2 *', '1 2 /', '2 3 / 1 +']
    for expr in allexpr:
        rv = postfix(expr)
        print("The expression “{}” evaluates to {}.".format(expr, rv))

if __name__ == '__main__':
    test()
