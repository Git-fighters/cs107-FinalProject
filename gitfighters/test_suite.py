# This file is meant as a demo and early testing tool

from git_fighters import *
import pytest


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

def test_equality():
    x1 = fightingAD(10)
    x2 = fightingAD(10) + 3 - 3
    try:
        assert x1 == 5
    except TypeError:
        assert x1 == x2


def test_inequality():
    x1 = fightingAD(5)
    x2 = fightingAD(5) + 3 
    try:
        assert x1 != 5
    except TypeError:
        assert x1 != x2


def test_addition():
    x1 = fightingAD(3)
    x1 = x1 + 5
    assert x1.val == 8
    assert x1.der == 1

    x2 = fightingAD(3)
    x3 = x1 + x2
    assert x3.val == 11
    assert x3.der == 2


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
    assert x3.der == -8  # derivative should be 2 here. this gives error


def test_neg():
    x1 = fightingAD(5)
    x2 = -x1
    assert x2.val == -5
    assert x2.der == -1


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


def test_pow():
    x1 = fightingAD(5)
    x2 = x1 ** 2
    assert x2.val == 25
    assert x2.der == 10

    x1 = fightingAD(5)
    x2 = x1 * 2
    x3 = x1 ** x2
    assert x3.val == 9765625
    #assert x3.der == 25482792.11361426

    x1 = fightingAD(0)
    x2 = x1 ** 5
    assert x2.val == 0
    assert x2.der == 0

    x1 = fightingAD(5)
    x2 = x1 ** (-3)
    assert x2.val == 0.008
    assert round(x2.der, 4)  == -0.0048

    x1 = fightingAD(0)
    x2 = x1 ** (-35)
    assert x2.val == 0
    assert x2.der == 0

    x1 = fightingAD(5)
    x2 = 2**x1
    assert x2.val == 32
    #assert x2.der == 80

    x1 = fightingAD(2)
    x2 = 2**(x1*2)
    assert x2.val == 16
    #assert x2.der == 32 * log(2)

    x1 = fightingAD(5)
    x2 = 0**x1
    assert x2.val == 0
    assert x2.der == 0

def test_pow1():

    x = fightingAD(2)
    f = x**2
    assert f.val == 4
    assert f.der == 4

def test_pow2():
    x = fightingAD(2)
    f = 2**x
    assert f.val == 4
    assert f.der == np.log(2) * 4


def test_pow3():
    x = fightingAD(2)
    f = x**x
    assert f.val == 4
    assert f.der == np.log(2) * 4 + 4


def test_pow4():
    x = fightingAD(3)
    f = x**(x-2)
    assert f.val == 3
    assert f.der == np.log(3)*3 + 1

def test_pow5():
    x = fightingAD(3)
    f = (x-2)**x
    assert f.val == 1
    assert f.der == 3


def test_abs():
    x1 = fightingAD(0.54, -0.84)
    x2 = abs(x1)
    assert x2.val == 0.54
    assert x2.der == 0.84

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


def test_log():
    x1 = fightingAD(5)
    x2 = log(x1)
    x2.val = 0.69897000433

    x1 = fightingAD(5)
    x2 = log(2)
    x2 = 0.30102999566



def test_other_elementary():
    pass


def test_combined():
    pass


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
        return x**(1/2) + log(x) - x**5 + x/x**2 + sin(cos(x))
    x1 = fightingAD(3)
    y1 = f(x1)
    assert y1.val == float(-(728/3) + 3**(1/2) + log(3) + sin(cos(3)))
    assert y1.der == float((1/18) * (3 * 3**(1/2) - 7286) - sin(3)*cos(cos(3)))



# this newton function gives NameError. I tried to fix it, but it goes into an eternal loop
def test_newton():
    # initial root value

    x1 = fightingAD(2)
    st_condition = 1

    # Newton's method main loop
    while st_condition > 1e-16:
        y = x1 * x1 + sin(x1)
        xval = x1 - y.val/y.der
        x_old = np.copy(x1.val)
        x1 = fightingAD(xval.val)
        st_condition = np.abs(x1-x_old).val

    assert x1.val == 0
    print('Passed the Newton test')



