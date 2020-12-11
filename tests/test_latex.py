from gitfighters.latex import *


def test_create_cool_latex_jacobian():
    x = AD([1, 2, 3, 4])
    create_cool_latex_jacobian(x)
