##############################################################################
# This is where the tests that ensure correct functionality reside.
# Pytest executes each of these, and sends a report to TravisCI and Codecov,
# for an easy visualization. All of them must pass before a PR is approved.
# if new functionality is defined, please add appropriate test cases, such
# that coverage remains at 100%.
##############################################################################

from gitfighters.git_fighters import *
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
