#!/usr/bin/env python3

from gitfighters.git_fighters import *
from gitfighters.vector import *


def create_cool_latex_jacobian(x):
    """Takes in as input an AD object
    writes Jacobian to Jacobian.tex file
    returns latex String
    """

    startJac = r"$J_{ij} = \frac{\partial f_i}{\partial x_j} = \left[\begin{array}{cc}"
    startVec = r"$\frac{\partial f}{\partial x_i} = \left[\begin{array}{cc}"
    startDer = r"$\frac{\partial f}{\partial x} = "
    endJac = r"\ \end{array}\right]$"
    endDer = ""

    der = differentiate(x)
    dim = np.array(der).shape

    if dim == ():
        start = startDer
        jacobian = "\ {} $".format(der)
        end = endDer
    else:
        jacobian = ""
        try:
            start = startJac
            rows = 0
            while rows < dim[0]:
                for i in der[rows, :]:
                    jacobian += r"\ {}".format(i)
                rows += 1
                if rows < dim[0]:
                    jacobian += r"\\"
        except TypeError:
            for i in der:
                jacobian += r"\ {}".format(i)
            start = startVec
        end = endJac

    with open("jacobian.tex", "w") as file:
        file.write("\\documentclass{article}\n")
        file.write("\\begin{document}\n")
        file.write(start + jacobian + end + "\n")
        file.write("\\end{document}\n")

    return start + jacobian + end


# OLD
# from pylatexenc.latex2text import *
# from pylatexenc.latexwalker import LatexWalker


# def parse_latex(formula):

#     w = LatexWalker(formula)
#     (nodelist, pos, len_) = w.get_latex_nodes(pos=0)

#     l2t = LatexNodes2Text()
#     temp = l2t.nodelist_to_text(nodelist)
#     print(temp)


# parse_latex("$\\cos({w}) - \\frac{(y - 5)}{z} + e^{x}$")
