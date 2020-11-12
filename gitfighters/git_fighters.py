#!/usr/bin/env python3
# Package aiming to enable automatic differentiation with Python.
# By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

"""
Notes from Manana:

Check: __abs__ 

"""

import numpy as np


class fightingAD:

    # Constructor to set class up
    def __init__(self, value, derivative=1.0):
        self.val = value
        self.der = derivative

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
        return fightingAD(-self.val, -self.der)

    # Overload absolute value
    def __abs__(self):

        # derivative
        if self.val < 0:
            self.der = -self.der

        return fightingAD(np.abs(self.val), self.der)

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

    def __pow__(self, power):
        return fightingAD(self.val ** power, power * self.der ** (power - 1))

    def sin(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.sin(x.val)
        der = x.der*np.cos(x.val)
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.sin(x))

    def cos(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.cos(x.val)
        der = -x.der*np.sin(x.val)
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.cos(x))

    def tan(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.tan(x.val)
        der = x.der*np.cos(x.val)**2
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.tan(x))

    def arcsin(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.arcsin(x.val)
        der = x.der*(1/np.sqrt(1 - x.val**2))
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.arcsin(x))
    
    def arccos(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.arccos(x.val)
        der = -x.der*(1/np.sqrt(1 - x.val**2))
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.arccos(x))

    def arctan(x):
      # Check if the input is a fightingAD object or a constant
      try:
        val = np.arctan(x.val)
        der = x.der*(1/(1 + x.val**2))
        return fightingAD(val,der)
      except AttributeError:
        return fightingAD(np.arctan(x))
