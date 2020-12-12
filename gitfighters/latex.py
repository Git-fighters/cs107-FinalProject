#!/usr/bin/env python3

from git_fighters import *
from vector import *


def create_latex_file(der):
    
    startJac = r"$J_{ij} = \frac{\partial f_i}{\partial x_j} = \left[\begin{array}{cc}"
    startVec = r"$\frac{\partial f}{\partial x_i} = \left[\begin{array}{cc}"
    startDer = r"$\frac{\partial f}{\partial x} = "
    endJac = r"\ \end{array}\right]$"
    endDer = ""

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

    with open('jacobian.tex','w') as file:
        file.write('\\documentclass[12pt]{article}\n')
        file.write('\\usepackage{amsmath}\n')
        file.write('\\usepackage{graphicx}\n')
        file.write('\\graphicspath{ {./graphs/} }\n')
        file.write('\\title{Summary:}\n')
        file.write('\\begin{document}\n') 
        file.write(start + jacobian  + end + '\n')
        file.write('\\includegraphics{x_graph.png}\n')
        file.write('\\end{document}\n')


z = fightingAD(5, [1, 2, 3, 5])
create_latex_file(z)
