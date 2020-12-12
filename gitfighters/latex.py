#!/usr/bin/env python3

from datetime import datetime
import numpy as np


def create_latex_file(der, graph_names="", user_input=""):
    """
    This function creates a formatted LaTeX document.

    INPUTS:
    ======
    der: list of derivatives
    grap_names: list of graph_names
    user_input: optional user input - string
    """

    startJac = r"$J_{ij} = \frac{\partial f_i}{\partial x_j} = \left[\begin{array}{cc}"
    startVec = r"$\frac{\partial f}{\partial x_i} = \left[\begin{array}{cc}"
    startDer = r"$\frac{\partial f}{\partial x} = "
    endJac = r"\ \end{array}\right]$"
    endDer = ""

    dim = np.array(der).shape
    graphs = graph_names
    if np.array(graphs).shape == ():
        graphs = np.array([graphs])
    else:
        graphs = np.array(graphs)

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
        except (TypeError, IndexError):
            jacobian = ""
            for i in der:
                jacobian += r"\ {}".format(i)
            start = startVec
        end = endJac

    file_name = "jacobian_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".tex"
    with open(file_name, "w") as file:
        file.write("\\documentclass[12pt]{article}\n")
        file.write("\\usepackage{amsmath}\n")
        file.write("\\usepackage{graphicx}\n")
        file.write("\\usepackage{float}\n")
        file.write("\\graphicspath{ {../graphs/} }\n")
        file.write("\\title{Summary:}\n")
        file.write("\\begin{document}\n")
        file.write("\\maketitle\n")
        file.write("\\centering\n")
        file.write("\\section*{" + user_input + "}\n")
        file.write(start + jacobian + end + "\n")
        if graphs[0] != "":
            for graph in graphs:
                file.write("\\begin{figure}[H]\n")
                file.write("\\includegraphics[width=15cm]{" + graph + "}\n")
                file.write("\\end{figure}\n")
        file.write("\\end{document}\n")

    print(f"latex file created under {file_name}")
