#!/usr/bin/env python3
# Package aiming to enable automatic differentiation with Python.
# By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

import numpy as np


class fightingAD:
    """Main object of the git_fighters library.

    This class is used as the central building block of the git_fighters library.
    Creates a fightingAD objects supporting custom operations for Automatic Differentiation.

    Attributes
    ==========
    val : int, float
        The value of user defined function(s) 'f' evaluated at point 'x'.
        der : int, float
            The corresponding derivative of user defined functions(s) 'f' evaluated at point 'x'.
    """

    def __init__(self, value, derivative=1.0, name="x"):
        """
        INPUTS
        =======
        val : int, float
                The value of user defined function(s) 'f' evaluated at point 'x'.
        der : int, float, optional (default=1.0)
                The corresponding derivative of user defined functions(s) 'f' evaluated at point 'x'.

        EXAMPLES
        =========
        # Input a constant
        >>> fightingAD(1.0, None)
        AD: 1.0, None
        # Input a scalar variable
        >>> fightingAD(1.0)
        AD: 1.0, 1.0
        """
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

    def __str__(self):
        """Returns the string representation of the current fightingAD object.

        INPUTS
        =======
        self: the current fightingAD object

        RETURNS
        ========
        fightingAD: the string representation of the fightingAD object

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> print(x)
        AD object with value of 5 and derivative of 1.
        """
        return "AD object with value of {} and derivative of {}".format(
            self.val, self.der
        )

    def __repr__(self):
        """Returns the representation of the current fightingAD object.

        INPUTS
        =======
        self: the current fightingAD object

        RETURNS
        ========
        fightingAD: the representation of the fightingAD object

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> x.repr()
        AD: 5, 1
        """
        return "AD: {}, {}".format(self.val, self.der)

    def __eq__(self, other):
        """Equality method: Checks if this object is equal to another object.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object we are comparing to. Can be scalar or fightingAD object

        RETURNS
        ========
        True if equal, False otherwise

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> y = fightingAD(6)
        >>> x == y
        False
        """
        try:
            return (self.val == other.val) and (self.der == other.der).all()
        except:
            try:
                return (self.val == other.val) and (self.der == other.der)
            except:
                raise TypeError(
                    "unsupported operand type(s) for =: {} and {}".format(
                        type(self).__name__, type(other).__name__
                    )
                )

    def __ne__(self, other):
        """Inequality method: Checks if this object is not equal to another object.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object we are comparing to. Can be scalar or fightingAD object

        RETURNS
        ========
        True if NOT equal, False otherwise

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> y = fightingAD(6)
        >>> x != y
        True
        """
        try:
            return (self.val != other.val) or (self.der != other.der)
        except:
            raise TypeError(
                "unsupported operand type(s) for =: {} and {}".format(
                    type(self).__name__, type(other).__name__
                )
            )

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
        return fightingAD(abs(self.val), abs(self.der))

    def __pos__(self):
        """Returns a fightingAD object with the unary plus operator.

        INPUTS
        =======
        self: the current fightingAD object

        RETURNS
        ========
        fightingAD: new instance with absolute values of current val and der

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> +x
        5
        """
        return fightingAD(self.val, self.der)

    def __add__(self, other):
        """Addition operand: adds self to the other.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object we are adding to. Can be scalar or fightingAD object

        RETURNS
        ========
        new fightingAD object with added value and derivative

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> y = fightingAD(6)
        >>> s = x + y
        >>> print(s)
        AD object with value of 11 and derivative of 2
        """
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

    def __radd__(self, other):
        """Called when the left object does not have the __add__ method implemented.
        Since addition is commutative, we can swap the order and call __add__

        INPUTS
        =======
        other: scalar object to add

        RETURNS
        ========
        fightingAD: new instance with derivative and function values

        EXAMPLES
        =========
        >>> x = fightingAD(1)
        >>> x = 2 + x
        >>> print(x.val, x.der)
        3, 1
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Subraction operand: subtracts other from self.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object we are subracting, can be scalar or fightingAD object

        RETURNS
        ========
        new fightingAD object with subtracted value and derivative

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> y = fightingAD(6)
        >>> s = x - y
        >>> print(s)
        AD object with value of -1 and derivative of 0
        """
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

    def __rsub__(self, other):
        """Called when the left object does not have the __sub__ method implemented.
        Since subtraction can be represented as addition with negative object,
        we negate the right object, swap the order and call __add__

        INPUTS
        =======
        other: scalar object to subtract

        RETURNS
        ========
        fightingAD: new instance with derivative and function values

        EXAMPLES
        =========
        >>> x = fightingAD(1)
        >>> x = 2 - x
        >>> print(x.val, x.der)
        1, -1
        """
        return fightingAD(-self.val, -self.der).__add__(other)

    def __mul__(self, other):
        """Multiplication operand: multiplies self by other.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object to multiply with. Can be scalar or fightingAD object

        RETURNS
        ========
        new fightingAD object with multiplied value and derivative

        EXAMPLES
        =========
        >>> x = fightingAD(5)
        >>> y = fightingAD(6)
        >>> m = x * y
        >>> print(m)
        AD object with value of 30 and derivative of 11
        """
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

    def __rmul__(self, other):
        """Multiplies an fAD object.

        Used in case that the first value to be multiplied with is not an fAD object.
        Since multiplication is commutative, we can swap the order and call __mul__

        INPUTS
        =======
        other: object to multiply with, can be scalar or fAD object

        RETURNS
        ========
        fightingAD: new instance with multiplied derivative and function values

        EXAMPLES
        =========
        >>> x = fightingAD(1)
        >>> x = 2 * x
        >>> print(x.val, x.der)
        2, 2
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """Division operand: divides self by other.

        INPUTS
        =======
        self: the current fightingAD object
        other: The object to divide with. Can be scalar or fightingAD object

        RETURNS
        ========
        new fightingAD object with divided value and derivative.

        EXAMPLES
        =========
        >>> x = fightingAD(30)
        >>> y = fightingAD(6)
        >>> d = x / y
        >>> print(d)
        AD object with value of 5 and derivative of -25/36??????
        """
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

    def __rtruediv__(self, other):
        """Divides a non-fAD object by a fAD object.

        Is called when the first operand in a division is a scalar.

        INPUTS
        =======
        other: object to divide with, is scalar/vector

        RETURNS
        ========
        fightingAD: new instance with divided derivative and function values

        EXAMPLES
        =========
        >>> x1 = fightingAD(10)
        >>> y = 2 / x
        >>> print(y.val)
        0.2
        """
        try:
            return fightingAD(other, derivative=0).__truediv__(self)
        except:
            raise Exception("unsupported operation for /")

    def __pow__(self, other):
        """Returns a fightingAD object with the power of the currenct object.

        INPUTS
        =======
        self: base (the current fightingAD object)
        other: exponent
        f(g(x)) = f'(g(x))* g'(x)

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
            try:
                if other.val < 0:
                    raise ZeroDivisionError("0.0 cannot be raised to a negative power")
                else:
                    return fightingAD(0, 0)
            except AttributeError:
                if other < 0:
                    raise ZeroDivisionError("0.0 cannot be raised to a negative power")
                else:
                    return fightingAD(0, 0)
        else:
            try:
                return fightingAD(
                    self.val ** other.val,
                    np.log(self.val) * self.val ** other.val * other.der
                    + other.val * self.der * self.val ** (other.val - 1),
                )
            except AttributeError:
                try:
                    return fightingAD(
                        self.val ** other, other * self.val ** (other - 1) * self.der
                    )
                except:
                    raise TypeError(
                        "unsupported operand type(s) for **: {} and {}".format(
                            type(self).__name__, type(other).__name__
                        )
                    )

    def __rpow__(self, other):
        """Returns an object with the power of the value of another class.

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
            if self.val < 0:
                raise ZeroDivisionError("0.0 cannot be raised to a negative power")
            else:
                return fightingAD(0, 0)
        else:
            try:
                return fightingAD(
                    other ** self.val, np.log(other) * other ** self.val * self.der
                )
            except:
                raise Exception("unsupported operation for **")


##############################
#### FUNCTION DEFINITIONS ####
##############################


def sqrt(x):
    """Returns the positive square-root of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    =======
    fightingAD: new instance with positive square-root of the current object

    EXAMPLES
    =========
    >>> x = fightingAD(9)
    >>> f = sqrt(x)
    >>> f.val
    3
    """
    try:
        if x.val < 0:
            return float("NaN")
        else:
            return fightingAD(x.val, x.der).__pow__(0.5)
    except AttributeError:
        if x < 0:
            return float("NaN")
        else:
            return np.sqrt(x)


def log(x):
    """Returns the natural log of the current object.

    INPUTS
    =======
    x: an object

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
            return fightingAD(np.log(x.val), 1 / x.val * x.der)
    except AttributeError:
        if x == 0:
            raise ValueError("log(0) is undefined")
        else:
            return np.log(x)


def exp(x):
    """Returns the exponential of the current object: e^x.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the exponential of the current object

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = exp(x)
    >>> f.val
    148.413159103
    """
    try:
        if x.val == 0:
            return fightingAD(1, 0)
        else:
            return fightingAD(np.exp(x.val), np.exp(x.val) * x.der)
    except AttributeError:
        if x == 0:
            return fightingAD(1, 0)
        else:
            return np.exp(x)


def sigmoid(x):
    """Returns the value of the logistic sigmoid function at x.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the value of the logistic sigmoid function at x.

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = sigmoid(x)
    >>> f.val
    0.99330714907
    """
    try:
        val = 1 / (1 + np.exp(-x.val))
        der = val * (1 - val) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return 1 / (1 + np.exp(-x))


def sin(x):
    """Returns the sine of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with sine of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(np.pi/2)
    >>> f = sin(x)
    >>> print(f)
    AD object with value of 1.0 and derivative of 6.123233995736766e-17
    """
    try:
        val = np.sin(x.val)
        der = x.der * np.cos(x.val)
        return fightingAD(val, der)
    except AttributeError:
        return np.sin(x)


def cos(x):
    """Returns the cosine of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with cosine of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(np.pi)
    >>> f = cos(x)
    >>> print(f)
    AD object with value of -1.0 and derivative of -1.2246467991473532e-16
    """
    try:
        val = np.cos(x.val)
        der = -x.der * np.sin(x.val)
        return fightingAD(val, der)
    except AttributeError:
        return np.cos(x)


def tan(x):
    """Returns the tangent of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with tangent of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(np.pi/4)
    >>> f = tan(x)
    >>> print(f)
    AD object with value of 0.9999999999999999 and derivative of 0.5000000000000001
    """
    try:
        val = np.tan(x.val)
        der = x.der * np.cos(x.val) ** 2
        return fightingAD(val, der)
    except AttributeError:
        return np.tan(x)


def arcsin(x):
    """Returns the arcsine of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with arcsine of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(0.5)
    >>> f = arcsin(x)
    >>> print(f)
    AD object with value of 0.5235987755982988 and derivative of 1.1547005383792517
    """
    try:
        val = np.arcsin(x.val)
        der = x.der * (1 / np.sqrt(1 - x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return np.arcsin(x)


def arccos(x):
    """Returns the arccosine of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with arccosine of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(0.5)
    >>> f = arccos(x)
    >>> print(f)
    AD object with value of 1.0471975511965979 and derivative of -1.1547005383792517
    """
    try:
        val = np.arccos(x.val)
        der = -x.der * (1 / np.sqrt(1 - x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return np.arccos(x)


def arctan(x):
    """Returns the arctangent of the current object.

    INPUTS
    =======
    x: fAD object or scalar

    RETURNS
    ========
    fightingAD: new instance with arctangent of the current object or scalar

    EXAMPLES
    =========
    >>> x = fightingAD(1)
    >>> f = arctan(x)
    >>> print(f)
    AD object with value of 0.7853981633974483 and derivative of 0.5
    """
    try:
        val = np.arctan(x.val)
        der = x.der * (1 / (1 + x.val ** 2))
        return fightingAD(val, der)
    except AttributeError:
        return np.arctan(x)


def sinh(x):
    """Returns the hyperbolic sine value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the hyperbolic sine value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = sinh(x)
    >>> f.val
    74.20321
    """
    try:
        val = np.sinh(x.val)
        der = np.cosh(x.val) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.sinh(x)


def cosh(x):
    """Returns the hyperbolic cosine value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the hyperbolic cosine value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = cosh(x)
    >>> f.val
    74.2099485248
    """
    try:
        val = np.cosh(x.val)
        der = np.sinh(x.val) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.cosh(x)


def tanh(x):
    """Returns the hyperbolic tangent value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the hyperbolic tangent value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(5)
    >>> f = tanh(x)
    >>> f.val
    0.99990920426
    """
    try:
        val = np.tanh(x.val)
        der = (1 - (np.sinh(x.val) ** 2 / np.cosh(x.val) ** 2)) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.tanh(x)


def arcsinh(x):
    """Returns the inverse hyperbolic sine value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the inverse hyperbolic sine value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(0.5)
    >>> f = arcsinh(x)
    >>> f.val
    0.4812118250596034
    """
    try:
        val = np.arcsinh(x.val)
        der = (1 / (np.sqrt(x.val ** 2 + 1))) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.arcsinh(x)


def arccosh(x):
    """Returns the inverse hyperbolic cosine value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the inverse hyperbolic cosine value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(1.5)
    >>> f = arccosh(x)
    >>> f.val
    0.9624236501192069
    """
    try:
        val = np.arccosh(x.val)
        der = (1 / (np.sqrt(x.val ** 2 - 1))) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.arccosh(x)


def arctanh(x):
    """Returns the inverse hyperbolic tangent value of the current object.

    INPUTS
    =======
    x: an object

    RETURNS
    ========
    fightingAD: new instance with the inverse hyperbolic tangent value of the current object.

    EXAMPLES
    =========
    >>> x = fightingAD(0.5)
    >>> f = arctanh(x)
    >>> f.val
    0.5493061443340549
    """
    try:
        val = np.arctanh(x.val)
        der = (-1 / (x.val ** 2 - 1)) * x.der
        return fightingAD(val, der)
    except AttributeError:
        return np.arctanh(x)
