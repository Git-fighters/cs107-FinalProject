#!/usr/bin/env python3

import ast 
from git_fighters import *
from pylatexenc.latex2text import *
from pylatexenc.latexwalker import LatexWalker


def parse_latex(formula):
    w = LatexWalker(formula)
    (nodelist, pos, len_) = w.get_latex_nodes(pos=0)

    l2t = LatexNodes2Text()
    temp = l2t.nodelist_to_text(nodelist)
    print(temp)


def create_cool_latex_jacobian(x):

    startJac = '$J_{ij} = \frac{\partial f_i}{\partial x_j} = $'
    startDer = '$\frac{\partial f}{\partial x} = $'

    der = differentiate(x)

    #with open('jabobian.tex','w') as file:
    #    file.write('\\documentclass{article}\n')
    #    file.write('\\begin{document}\n') 
    #    file.write(start+'\n')
    #    file.write('\\end{document}\n')

x = fightingAD(5)
create_cool_latex_jacobian(x)



