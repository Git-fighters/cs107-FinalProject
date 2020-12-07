##############################################################################
# This is where the tests that ensure correct functionality reside.
# Pytest executes each of these, and sends a report to TravisCI and Codecov,
# for an easy visualization. All of them must pass before a PR is approved.
# if new functionality is defined, please add appropriate test cases, such
# that coverage remains at 100%.
##############################################################################

from gitfighters.git_fighters import *
from gitfighters.vector import *
import numpy as np
import pytest


##########################
######### Basic ##########
##########################

def test_constructor():
    x1 = AD(1)
    assert x1.values == 1
    assert x1.derivatives == 1
