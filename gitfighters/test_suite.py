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
    pass


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
