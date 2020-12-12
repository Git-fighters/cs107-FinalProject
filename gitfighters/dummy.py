#!/usr/bin/env python3

from sympy import latex

# v0 = Variable('w', 1)
# v1 = Variable('x', 5)
# v2 = Variable('y', 3)
# v3 = Variable('z', 7)

o0 = latex((v0 / v1) * v2 ** 2 + sin(v3))
print(o0)
