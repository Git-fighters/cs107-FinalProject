#!/usr/bin/env python3
# Package aiming to enable automatic differentiation with Python.
# By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

"""
Notes from Manana:

Check: __abs__ 

Notes from Hugo:
- why do we always instantiate a new object in every method call? Why not modify inplace and return self?

Notes from Golo:
- Documentation should follow PEP 257 because it was mentioned in class
- I think the old implementation of __abs__ was problematic (if self.val < 0: self.der = -self.der). The val might be positive and the der negative (like f(x) = cos(x)). The old implementation would not have changed der.
- Please check my pow implementation. It run into computer impression problems.
- I do not think that there is a __log__ function in python :-)
- We should consider a gitignore file
- We assume that the derivative of integers in functions, like sin or log, is 1. Are we fine with this assumption?
"""

import numpy as np


class fightingAD():
    """Example Google style docstrings.

    This class is used as the central building block of the git_fighters library.

    Example Usage:
            $ ...
            $ ...
            >>> ...

    TODO:
        * Document all methods properly and show example usecases
        * Extend testing

    """

    # Constructor to set class up
    def __init__(self, value, derivative=1.0):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (float): point at which to evaluate the function
            derivative (float, optional): Derivative
                lines are supported.

        """
        self.val = value
        self.der = derivative
        # COMMENT: I think this should be ```self.der = derivative * value```
        # Or something similar. As it stands now it is problematic for a few things (like __pow__)

    # Overload str
    def __str__(self):
        return "AD object with value of {} and derivative of {}".format(
            self.val, self.der
        )

    # Overload repr
    def __repr__(self):
        return "AD: {}, {}".format(self.val, self.der)

    # Overload eq
    def __eq__(self, other):
        """Equality method
        Checks if this object is equal to another object

        Args:
            other: The object we are comparing to. Can be scalar or fightingAD object

        Returns:
            True if equal, False otherwise.

        """
        try:
            return (self.val == other.val) and (self.der == other.der)
        except:
            raise TypeError(
                "unsupported operand type(s) for =: {} and {}".format(
                    type(self).__name__, type(other).__name__
                )
            )

    # Overload ne
    def __ne__(self, other):
        try:
            return (self.val != other.val) or (self.der != other.der)
        except:
            raise TypeError(
                "unsupported operand type(s) for =: {} and {}".format(
                    type(self).__name__, type(other).__name__
                )
            )

    # Overload negation
    def __neg__(self):
        """Returns the negation of the current fightingAD object.

        INPUTS
        =======
        self: the current fightingAD object

        RETURNS
        ========
        fightingAD: new instance with negation of current val and der

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> f = -x
        >>> f.val
        -5
        """
        return fightingAD(-self.val, -self.der)

    # Overload absolute value
    def __abs__(self):
        """Returns a fightingAD object with the absolute values of val and der.

        INPUTS
        =======
        self: the current fightingAD object

        RETURNS
        ========
        fightingAD: new instance with absolute values of current val and der

        EXAMPLES
        =========
        >>> x = fightingAD(0.54, -0.84)
        >>> f = abs(x)
        >>> f.der
        0.84
        """
        if self.val < 0:
            self.val = -self.val
        if self.der < 0:
            self.der = -self.der
        return fightingAD(self.val, self.der)

    # Overload pos
    def __pos__(self):
        return fightingAD(self.val, self.der)

    # Overload addition
    def __add__(self, other):
        try:
            return fightingAD(self.val + other.val, self.der + other.der)
        except AttributeError:
            try:
                return fightingAD(self.val + other, self.der)
            except:
                raise TypeError(
                    "unsupported operand type(s) for +: {} and {}".format(
                        type(self).__name__, type(other).__name__
                    )
                )
        else:
            raise Exception("unsupported operation for +")

    # Overload addition with reversed operands
    def __radd__(self, other):
        return self.__add__(other)

    # Overload subtraction
    def __sub__(self, other):
        try:
            return fightingAD(self.val - other.val, self.der - other.der)
        except AttributeError:
            try:
                return fightingAD(self.val - other, self.der)
            except:
                raise TypeError(
                    "unsupported operand type(s) for -: {} and {}".format(
                        type(self).__name__, type(other).__name__
                    )
                )
        else:
            raise Exception("unsupported operation for -")

    # Overload subtraction with reversed operand by negating values
    def __rsub__(self, other):
        return fightingAD(-self.val, -self.der).__add__(other)

    # Overload multiplication
    def __mul__(self, other):
        try:
            return fightingAD(
                self.val * other.val, self.val * other.der + self.der * other.val
            )
        except AttributeError:
            try:
                return fightingAD(self.val * other, self.der * other)
            except:
                raise TypeError(
                    "unsupported operand type(s) for *: {} and {}".format(
                        type(self).__name__, type(other).__name__
                    )
                )
        else:
            raise Exception("unsupported operation for *")

    # Overload multiplication with reversed operand
    def __rmul__(self, other):
        return self.__mul__(other)

    # Overload division
    def __truediv__(self, other):
        try:
            if other.val == 0:
                raise ZeroDivisionError("division by zero")
            return fightingAD(
                self.val / other.val,
                (self.der * other.val - self.val * other.der) / (other.val * other.val),
            )
        except AttributeError:
            try:
                return fightingAD(self.val / other, self.der / other)
            except Exception as e:
                raise TypeError(
                    "unsupported operand type(s) for /: {} and {}, e={}".format(
                        type(self).__name__, type(other).__name__, e
                    )
                )

    # Overload division with reversed operand
    def __rtruediv__(self, other):
        try:
            return fightingAD(other, derivative=0).__truediv__(self)
        except:
            raise Exception("unsupported operation for /")


    # Overload pow
    def __pow__(self, other):
        """Returns a fightingAD object with the power of the currenct object

        INPUTS
        =======
        self: base (the current fightingAD object)
        other: exponent

        RETURNS
        ========
        fightingAD: new instance with power of current val and der

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> f = x**2
        >>> f.val
        25
        """
        if self.val == 0:
            return fightingAD(0,0)
        try:
            if other.val == 0:
                return fightingAD(1, 0)
            return fightingAD(
                self.val ** other.val, 
                (np.log(self.val) + 1) * self.val ** other.val
            )
        except AttributeError:
            try:
                if other == 0:
                    return fightingAD(1, 0)
                return fightingAD(
                    self.val ** other, other * self.val ** (other -1)
                )
            except:
                raise TypeError(
                    "unsupported operand type(s) for **: {} and {}".format(
                        type(self).__name__, type(other).__name__
                    )
                )
        else:
            raise Exception("unsupported operation for **")

    def __rpow__(self, other):
        """Returns an object with the power of the value of another class

        INPUTS
        =======
        self: exponent (value of a fightingAD object)
        other: base (value of other class such as integer) 

        RETURNS
        ========
        fightingAD: new instance with power of the value of another class

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> f = 2**x
        >>> f.val
        32
        """
        if other == 0:
            return fightingAD(0, 0)
        elif self.val == 0:
            return fightingAD(1, 0)
        else:
            try:
                return fightingAD(
                    other ** self.val, self.val * other ** (self.val -1)
                )
            except:
                raise Exception("unsupported operation for **")

    # EXAMPLE OF HOW FUNCTIONS WOULD BE IF WE CHANGED VALUES IN PLACE:
    # YOU CAN SEE A BENCHMARK in benchmark.py
    def __pow2__(self, power):
        self.val = self.val ** power
        self.der = power * self.der ** (power - 1)
        return self

    def __mul2__(self, other):
        self.val = self.val * other.val
        self.der = self.val * other.der + self.der * other.val
        return self



# FUNCTION DEFINITIONS
# 

def log(x):
    """Returns the natural log of the current object.

    INPUTS
    =======
    x: fightingAD object

    RETURNS
    ========
    fightingAD: new instance with natural log of the current object

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = log(x)
    >>> f.val
    0.69897
    """
    try:
        if x.val == 0:
            raise ValueError("log(0) is undefined")
        else:    
            return fightingAD(np.log(x.val), 1 / x.val)
    except AttributeError:
        return fightingAD(np.log(x))


def sin(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.sin(x.val)
        der = x.der * np.cos(x.val)
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.sin(x))

def cos(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.cos(x.val)
        der = -x.der * np.sin(x.val)
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.cos(x))

def tan(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.tan(x.val)
        der = x.der * np.cos(x.val) ** 2
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.tan(x))

def arcsin(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.arcsin(x.val)
        der = x.der * (1 / np.sqrt(1 - x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.arcsin(x))

def arccos(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.arccos(x.val)
        der = -x.der * (1 / np.sqrt(1 - x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.arccos(x))

def arctan(x):
    # Check if the input is a fightingAD object or a constant
    try:
        val = np.arctan(x.val)
        der = x.der * (1 / (1 + x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return fightingAD(np.arctan(x))
