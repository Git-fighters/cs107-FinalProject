# This file is meant as a demo and early testing tool

from git_fighters import *
import pytest


def test_basic():
    x = fightingAD(3)
    assert x.val == 3
    assert x.der == 1


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
    x1 = fightingAD(np.pi/2)
    x2 = fightingAD(np.pi/4)

    assert fightingAD.sin(x1).val == 1 
    assert fightingAD.sin(x1).der <= 1e-16 # Expected value 0 (to machine precision)
    
    assert fightingAD.cos(x1).val <= 1e-16 # Expected value 0 (to machine precision)
    assert fightingAD.cos(x1).der == -1

    assert fightingAD.tan(x2).val == 1-1e-16 # Expected value 1 (to machine precision)
    assert fightingAD.tan(x2).der == 0.5+1e-16 # Expected value 0.5 (to machine precision)
    
    assert fightingAD.arcsin(x2).val == 0.9033391107665127
    assert fightingAD.arcsin(x2).der == 1.6155326551693476
    
    assert fightingAD.arccos(x2).val == 0.6674572160283838
    assert fightingAD.arccos(x2).der == -1.6155326551693476
    
    assert fightingAD.arctan(x2).val == 0.6657737500283538
    assert fightingAD.arctan(x2).der == 0.6184864581588363


def test_pow():
    x1 = fightingAD(5)
    x2 = x1 ** 2
    assert x2.val == 25
    assert x2.der == 2

    pass


def test_exp():
    pass


def test_log():
    pass


def test_other_elementary():
    pass


def test_combined():
    pass


def test_general():
    pass

def test_newton():
    # initial root value
    x = fightingAD(2)
    st_condition = 1

    # Newton's method main loop
    while st_condition > 1e-16:
        y = x1 * x1 + fightingAD.sin(x1)
        xval = x1 - y.val/y.der
        x_old = np.copy(x1.val)
        x = fightingAD(xval.val)
        st_condition = np.abs(x-x_old).val

    assert x.val == 0

