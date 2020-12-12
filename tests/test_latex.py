##############################################################################
# This is where the tests that ensure correct functionality reside.
# Pytest executes each of these, and sends a report to TravisCI and Codecov,
# for an easy visualization. All of them must pass before a PR is approved.
# if new functionality is defined, please add appropriate test cases, such
# that coverage remains at 100%.
##############################################################################

from gitfighters.git_fighters import *
from gitfighters.visualize import *
from gitfighters.parsing import *
from gitfighters.vector import *
from gitfighters.latex import *
import pytest

##########################
######### Basic ##########
##########################


def test_latex():
    x1 = fightingAD(0)
    x2 = differentiate(x1)
    create_latex_file(x2, graph_names="x_graph", user_input="sin(x)")

    x1 = fightingAD(0, [1, 2])
    x2 = differentiate(x1)
    create_latex_file(x2, graph_names="x_graph", user_input="sin(x) + 5y")

    user_input = "x^2 + y^2 when x is 1 and y is 2"
    eq, vals = pipeline(user_input)
    vect = AD(list(vals.values()))
    for key, val in vals.items():
        values = list(vals.values())
        ind = values.index(val)
        ad = vect[ind]
        globals()[f"{key}"] = ad

    exec(f"global f; f = {eq}")

    derivatives = differentiate(f)
    values = evaluate(f)

    derivatives_dict = {key: derivatives[i] for i, key in enumerate(vals)}

    graph_names = visualize(eq, vals, derivatives_dict)
    create_latex_file(derivatives, graph_names)
