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
    assert x1.val == 1
    assert x1.der == 1
    assert x1.ads == fightingAD(1)

    x1 = AD(1, -5)
    assert x1.val == 1
    assert x1.der == -5
    assert x1.ads == fightingAD(1, -5)

    x1 = AD([1, 2])
    assert x1.val[0] == 1
    assert x1.der[0][1] == 0

    x1 = AD([1, 2], [3, 4])
    assert x1.ads[0].val == 1
    assert x1.ads[0].der[0] == 3

    with pytest.raises(Exception):
        x1 = AD([1, 2], [1, 2, 3])


def test_str():
    x1 = AD([1, 2])
    x2 = x1.__str__()
    assert (
        x2 == "AD object with value of [1 2] and derivative of [[1.0, 0.0], [0.0, 1.0]]"
    )


def test_repr():
    x1 = AD([1, 2])
    x2 = x1.__repr__()
    assert x2 == "AD: [1 2], [[1.0, 0.0], [0.0, 1.0]]"


##########################
###### Operations ########
##########################


def test_equality():
    x1 = AD([1, 2])
    x2 = AD([1, 2], [1, 1])
    assert x1 == x2
    assert not (x1 != x2)

    x1 = AD([1, 2])
    x2 = AD([3, 4])
    assert x1 != x2
    assert not (x1 == x2)

    with pytest.raises(TypeError):
        x1 = AD([1, 2])
        x1 == 5

    with pytest.raises(TypeError):
        x1 = AD([1, 2])
        x1 != 5


def test_neg():
    x1 = AD([-1, 2], [-3, 5])
    x2 = -x1
    assert x2.val[0] == 1
    assert x2.val[1] == -2
    assert x2.der[0][0] == 3
    assert x2.der[1][1] == -5
    assert x2.ads[0].val == 1


def test_pos():
    x1 = AD([2, 3, 4], [4, 1, 3])
    x2 = +x1
    assert x2.val[0] == 2
    assert x2.der[0][0] == 4
    assert x2.der[1][1] == 1
    assert x2.der[2][2] == 3


def test_abs():
    x1 = AD([-1, 2])
    x2 = abs(x1)
    assert x2.val[0] == 1
    assert x2.val[1] == 2
    assert x2.der[0][0] == 1
    assert x2.der[1][1] == 1


##########################
##### Iterator Test ######
##########################


def test_iterator():
    i = -1
    y = np.array([1, 2, 3, 4, 5])
    x1 = AD(y)

    for AD_obj in x1:
        i += 1
        assert AD_obj.val == y[i]


##########################
###### set/get item ######
##########################


def test_get():
    x = AD([1, 2, -5])
    assert x[0] == x.ads[0]
    assert x[1] == x.ads[1]
    assert x[2] == x.ads[2]


def test_set():
    x = AD([1, 2, 3], [9, 9, 9])
    x[1] = fightingAD(5)
    assert x[1].val == 5
    assert x.val[1] == 5
    assert x.der[1][0] == 0
    assert x.der[1][1] == 1
    assert x.der[1][2] == 0
    assert x.der[0][0] == 9

    x = AD([1, 2, 3], [9, 9, 9])
    x[1] = fightingAD(5, [1, 1, 1])
    assert x[1].val == 5
    assert x.val[1] == 5
    assert x.der[1][0] == 1
    assert x.der[1][1] == 1
    assert x.der[1][2] == 1
    assert x.der[0][0] == 9

    x = AD(1, 5)
    x[0] = fightingAD(5)
    assert x[0].val == 5
    assert x.val == 5
    assert x.der == 1

    with pytest.raises(TypeError):
        x = AD([1, 2, 3], [9, 9, 9])
        x[1] = "String"

    with pytest.raises(TypeError):
        x = AD([1, 2, 3], [9, 9, 9])
        x[1] = 5


def test_del():
    x = AD([1, 2, 3], [9, 9, 9])
    del x[1]
    assert x[0].val == 1
    assert x.val[1] == 3
    assert x.der[0][0] == 9
    assert x.der[0][1] == 0
    assert x.der[1][0] == 0
    assert x.der[1][1] == 9

    with pytest.raises(IndexError):
        x = AD([1, 2, 3], [9, 9, 9])
        del x[3]


##########################
# Evaluate/Differentiate #
##########################

def test_eval():
    x1 = fightingAD(1, 5)
    x2 = evaluate(x1)
    assert x2 == x1.val

    with pytest.raises(Exception):
        evaluate('String')

def test_diff():
    x1 = fightingAD(1, 5)
    x2 = differentiate(x1)
    assert x2 == x1.der 

    with pytest.raises(Exception):
        differentiate('String')
