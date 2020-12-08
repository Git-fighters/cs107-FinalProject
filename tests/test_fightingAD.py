##############################################################################
# This is where the tests that ensure correct functionality reside.
# Pytest executes each of these, and sends a report to TravisCI and Codecov,
# for an easy visualization. All of them must pass before a PR is approved.
# if new functionality is defined, please add appropriate test cases, such
# that coverage remains at 100%.
##############################################################################

import numpy as np
import pytest
from gitfighters.git_fighters import *

##########################
######### Basic ##########
##########################


def test_constructor():
    x = fightingAD(3)
    assert x.val == 3
    assert x.der == 1


def test_str():
    x = fightingAD(5, 1)
    a = x.__str__()
    assert a == "AD object with value of 5 and derivative of 1"


def test_repr():
    x = fightingAD(5, 1)
    a = x.__repr__()
    assert a == "AD: 5, 1"


##########################
###### Operations ########
##########################


def test_abs():
    x1 = fightingAD(0.54, -0.84)
    x2 = abs(x1)
    assert x2.val == 0.54
    assert x2.der == 0.84


def test_equality():
    x1 = fightingAD(10)
    x2 = fightingAD(10) + 3 - 3
    assert x1 == x2
    with pytest.raises(TypeError):
        x1 == 5


def test_inequality():
    x1 = fightingAD(5)
    x2 = fightingAD(5) + 3
    assert x1 != x2
    with pytest.raises(TypeError):
        x1 != 5


def test_addition():
    x1 = fightingAD(3)
    x1 = x1 + 5
    x2 = 3 + x1
    assert x2.val == 11
    assert x2.der == 1
    assert x1.val == 8
    assert x1.der == 1

    x3 = fightingAD(3)
    x4 = x1 + x3
    assert x4.val == 11
    assert x4.der == 2

    x4 = 2 + x2
    assert x4.val == 13
    assert x4.der == 1

    with pytest.raises(TypeError):
        x2 + "String"


def test_subtraction():
    x1 = fightingAD(3)
    x2 = 5 - x1
    assert x2.val == 2
    assert x2.der == -1

    with pytest.raises(TypeError):
        x1 - "String"


def test_multiplication():
    x1 = fightingAD(-4)
    x2 = x1 * 3
    assert x2.val == -12
    assert x2.der == 3

    x2 = 3 * x1
    assert x2.val == -12
    assert x2.der == 3

    x2 = fightingAD(-4)
    x3 = x1 * x2
    assert x3.val == 16
    assert x3.der == -8

    with pytest.raises(TypeError):
        x2 * "String"


def test_neg():
    x1 = fightingAD(5)
    x2 = -x1
    assert x2.val == -5
    assert x2.der == -1


def test_pos():
    x1 = fightingAD(-1)
    x2 = +x1
    assert x2.val == -1

    x1 = fightingAD(1)
    assert +x1.val == 1


def test_division():
    x1 = fightingAD(5)
    x2 = x1.__truediv__(2)
    assert x2.val == 2.5
    assert x2.der == 0.5

    x1 = fightingAD(5)
    x2 = x1 / 2
    assert x2.val == 2.5
    assert x2.der == 0.5

    x1 = fightingAD(5)
    x2 = 2 / x1
    assert x2.val == 2 / 5
    assert x2.der == -1 * (2 / 25)

    x2 = fightingAD(5)
    x1 = fightingAD(0)
    with pytest.raises(ZeroDivisionError):
        x2 / x1

    with pytest.raises(TypeError):
        x2 / "String"

    with pytest.raises(Exception):
        5 / x1


##########################
###### Trigonometry ######
##########################


def test_trigonometry():
    x1 = fightingAD(np.pi / 2)
    x2 = fightingAD(np.pi / 4)

    assert sin(x1).val == 1
    assert sin(x1).der <= 1e-16  # Expected value 0 (to machine precision)

    assert cos(x1).val <= 1e-16  # Expected value 0 (to machine precision)
    assert cos(x1).der == -1

    assert tan(x2).val == 1 - 1e-16  # Expected value 1 (to machine precision)
    assert tan(x2).der == 0.5 + 1e-16  # Expected value 0.5 (to machine precision)

    assert arcsin(x2).val == 0.9033391107665127
    assert arcsin(x2).der == 1.6155326551693476

    assert arccos(x2).val == 0.6674572160283838
    assert arccos(x2).der == -1.6155326551693476

    assert arctan(x2).val == 0.6657737500283538
    assert arctan(x2).der == 0.6184864581588363

    assert sin(np.pi / 2) == 1
    assert cos(np.pi / 2) <= 1e-16  # Expected value 0 (to machine precision)
    assert tan(np.pi / 4) == 1 - 1e-16  # Expected value 1 (to machine precision)
    assert arcsin(np.pi / 4) == 0.9033391107665127
    assert arccos(np.pi / 4) == 0.6674572160283838
    assert arctan(np.pi / 4) == 0.6657737500283538


##########################
######### Power ##########
##########################


def test_pow():
    x1 = fightingAD(5)
    x2 = x1 ** 2
    assert x2.val == 25
    assert x2.der == 10

    x1 = fightingAD(5)
    x2 = x1 * 2
    x3 = x1 ** x2
    assert x3.val == 9765625
    assert x3.der == 19531250 * (1 + log(5))

    x1 = fightingAD(0)
    x2 = x1 ** 5
    assert x2.val == 0
    assert x2.der == 0

    x1 = fightingAD(0)
    x2 = fightingAD(5)
    x3 = x1 ** x2
    assert x3.val == 0
    assert x3.der == 0

    x1 = fightingAD(5)
    x2 = x1 ** (-3)
    assert x2.val == 0.008
    assert round(x2.der, 4) == -0.0048

    x1 = fightingAD(5)
    x2 = 2 ** x1
    assert x2.val == 32
    assert x2.der == 32 * log(2)

    x1 = fightingAD(2)
    x2 = 2 ** (x1 * 2)
    assert x2.val == 16
    assert x2.der == 32 * log(2)

    x1 = fightingAD(5)
    x2 = 0 ** x1
    assert x2.val == 0
    assert x2.der == 0

    x1 = fightingAD(5)
    x2 = x1 ** 0
    assert x2.val == 1
    assert x2.der == 0

    with pytest.raises(TypeError):
        x1 ** "String"

    with pytest.raises(Exception):
        fightingAD(0) ** (-5)

    with pytest.raises(Exception):
        0 ** fightingAD(-5)

    with pytest.raises(Exception):
        fightingAD(0) ** fightingAD(-5)

    with pytest.raises(Exception):
        "String" ** fightingAD(5)


def test_pow1():

    x = fightingAD(2)
    f = x ** 2
    assert f.val == 4
    assert f.der == 4


def test_pow2():
    x = fightingAD(2)
    f = 2 ** x
    assert f.val == 4
    assert f.der == np.log(2) * 4


def test_pow3():
    x = fightingAD(2)
    f = x ** x
    assert f.val == 4
    assert f.der == np.log(2) * 4 + 4


def test_pow4():
    x = fightingAD(3)
    f = x ** (x - 2)
    assert f.val == 3
    assert f.der == np.log(3) * 3 + 1


def test_pow5():
    x = fightingAD(3)
    f = (x - 2) ** x
    assert f.val == 1
    assert f.der == 3


##########################
########## e**x ##########
##########################


def test_exp():
    x1 = fightingAD(5)
    x2 = exp(x1)
    assert round(x2.val, 5) == 148.41316
    assert round(x2.der, 5) == 148.41316

    x1 = fightingAD(0)
    x2 = exp(x1)
    assert x2.val == 1
    assert x2.der == 0

    x1 = fightingAD(5)
    x2 = exp(5)
    assert round(x2, 5) == 148.41316

    assert exp(0) == fightingAD(1, 0)

    x1 = fightingAD(5)
    x2 = fightingAD(2)
    x3 = x1 * x2
    x4 = exp(x3)
    assert round(x4.val, 5) == 22026.46579
    assert round(x4.der, 5) == 154185.26056


##########################
####### logarithms #######
##########################


def test_log():
    x1 = fightingAD(5)
    x2 = log(x1)
    assert round(x2.val, 5) == 1.60944

    x1 = log(2)
    assert round(x1, 5) == 0.69315

    x1 = fightingAD(5)
    x2 = 2 * x1
    x3 = log(x2)
    assert round(x3.val, 5) == 2.30259
    assert x3.der == 0.2

    x = fightingAD(0)
    with pytest.raises(ValueError):
        log(x)

    with pytest.raises(ValueError):
        log(0)


##########################
####### sqare-root #######
##########################


def test_sqrt():
    x1 = sqrt(-1)
    x2 = np.isnan(x1)
    assert x2 == True

    x1 = sqrt(9)
    assert x1 == 3

    x1 = sqrt(fightingAD(-2))
    x2 = np.isnan(x1)
    assert x2 == True

    x1 = sqrt(fightingAD(4))
    assert x1.val == 2
    assert round(x1.der, 5) == 0.25

    x1 = fightingAD(3)
    x2 = x1 * x1
    x3 = sqrt(x2)
    assert x3.val == 3
    assert x3.der == 1

    ##########################
    ### logistic function ####
    ##########################

    x1 = fightingAD(5)
    x2 = sigmoid(x1)
    assert round(x2.val, 5) == 0.99331
    assert round(x2.der, 5) == 0.00665

    x1 = fightingAD(-5)
    x2 = sigmoid(x1)
    assert round(x2.val, 5) == 0.00669
    assert round(x2.der, 5) == 0.00665

    x1 = sigmoid(0)
    assert x1 == 0.5

    x1 = sigmoid(100000000)
    assert x1 == 1


##########################
## hyperbolic functions ##
##########################


def test_hyperbolic():

    x1 = fightingAD(5)
    x2 = sinh(x1)
    assert round(x2.val, 5) == 74.20321
    assert round(x2.der, 5) == 74.20995

    x1 = sinh(3)
    assert round(x1, 5) == 10.01787

    x1 = fightingAD(5)
    x2 = cosh(x1)
    assert round(x2.val, 5) == 74.20995
    assert round(x2.der, 5) == 74.20321

    x1 = cosh(3)
    assert round(x1, 5) == 10.06766

    x1 = fightingAD(5)
    x2 = tanh(x1)
    assert round(x2.val, 5) == 0.99991
    assert round(x2.der, 5) == 0.00018

    x1 = tanh(3)
    assert round(x1, 5) == 0.99505

    x1 = fightingAD(0.75)
    x2 = arcsinh(x1)
    assert round(x2.val, 5) == 0.69315
    assert round(x2.der, 5) == 0.8

    x1 = arcsinh(0.5)
    assert round(x1, 5) == 0.48121

    x1 = fightingAD(2)
    x2 = arccosh(x1)
    assert round(x2.val, 5) == 1.31696
    assert round(x2.der, 5) == 0.57735

    x1 = arccosh(1.5)
    assert round(x1, 5) == 0.96242

    x1 = fightingAD(0.5)
    x2 = arctanh(x1)
    assert round(x2.val, 5) == 0.54931
    assert round(x2.der, 5) == 1.33333

    x1 = arctanh(0)
    assert x1 == 0


##########################
######## General #########
##########################


def test_general():
    def f(x):
        return x ** 2 - x

    x1 = fightingAD(0)  # evaluate at x=0
    y1 = f(x1)
    assert y1.val == 0
    assert y1.der == -1

    x1 = fightingAD(3)  # evaluate at x=3
    y1 = f(x1)
    assert y1.val == 6
    assert y1.der == 5

    def f(x):
        return x ** 5 - x ** 3 + 2 * x

    x1 = fightingAD(0)  # evaluate at x=0
    y1 = f(x1)
    assert y1.val == 0
    assert y1.der == 2

    x1 = fightingAD(2)  # evaluate at x=2
    y1 = f(x1)
    assert y1.val == 28
    assert y1.der == 70

    def f(x):
        return x ** (1 / 2) + log(x) - x ** 5 + x / x ** 2 + sin(cos(x))

    x1 = fightingAD(3)
    y1 = f(x1)
    assert y1.val == float(-(728 / 3) + 3 ** (1 / 2) + log(3) + sin(cos(3)))
    assert y1.der == float((1 / 18) * (3 * 3 ** (1 / 2) - 7286) - sin(3) * cos(cos(3)))


def test_newton():
    # initial root value
    x1 = fightingAD(2)
    st_condition = 1

    # Newton's method main loop
    while st_condition > 1e-16:
        y = x1 * x1 + sin(x1)
        xval = x1 - y.val / y.der
        x_old = np.copy(x1.val)
        x1 = fightingAD(xval.val)
        st_condition = np.abs(x1 - x_old).val

    assert x1.val == 0


##########################
####### Edge cases #######
##########################


def test_wrong_input():
    a = "tale"
    b = fightingAD(1)
    with pytest.raises(TypeError):
        a * b
