#!/usr/bin/env python3

import ast 
from git_fighters import *
from pylatexenc.latex2text import *
from pylatexenc.latexwalker import LatexWalker


def parse_latex(formula):
    w = LatexWalker(repr(formula))
    (nodelist, pos, len_) = w.get_latex_nodes(pos=0)

    l2t = LatexNodes2Text()
    temp = l2t.nodelist_to_text(nodelist)
    print(temp)


parse_latex("$\cos({w}) - \frac{y - 5}{z} + e^{x}$")

