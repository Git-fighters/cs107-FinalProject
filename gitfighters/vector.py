#!/usr/bin/env python3
# Package aiming to enable automatic differentiation with Python.
# By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

import numpy as np
from gitfighters.git_fighters import *


class AD:
    """Main object to handle vector functions with multiple real scalar or vector inputs.

    Users will use this class to perform calculations on vector functions.
    It creates an AD objects supporting custom operations for Automatic Differentiation.

    Attributes
    ==========
    val : np.array
        Array storing n different variables to evaluate.
    der : np.array
        Arrary (n) or matrix (n x n) of derivatives. The default value is In.
    ads : np.array
        Array storing n different fightingAD objects representing the n variables.
    """

    def __init__(self, values, derivatives=None):
        """
        INPUTS
        =======
        values : np.array
            Array storing n different variables to evaluate.
        derivatives : np.array
            Array (n) or matrix (n x n) of derivatives. The default value is In.

        EXAMPLES
        =========
        # Input a constant
        >>> AD(1.0, None)
        AD: 1, None
        # Input a scalar variable
        >>> AD(1.0)
        AD: 1, [1]
        # Input a scalar variable
        >>> f = AD([1, 2])
        >>> f.val
        [1 2]
        >>> f.der
        [[1.0, 0.0]
         [0.0, 1.0]]
        """
        if np.array(values).shape == ():
            self.val = np.array([values])
        else:
            self.val = np.array(values)

        dim = len(list(self.val))
        der_matrix = np.identity(dim)
        self.ads = np.array([])

        if derivatives is not None:
            if np.array(derivatives).shape == ():
                self.der = np.array([derivatives])
            else:
                self.der = np.array(derivatives)
            if len(self.der) != len(self.val):
                raise Exception("derivatives and values not the same shape")
            der_matrix = der_matrix * self.der

        try:
            for i in range(dim):  # case where user provides derivatives
                der_matrix[i, i] = self.val[i].der
                self.ads = np.append(
                    self.ads, fightingAD(self.val[i].val, der_matrix[i, :])
                )
        except AttributeError:
            for i in range(dim):  # no user provided derivatives
                self.ads = np.append(
                    self.ads, fightingAD(self.val[i], der_matrix[i, :])
                )
        self.der = der_matrix

    def __str__(self):
        """Returns the string representation of the current AD object.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        AD: the string representation of the AD object

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> x.__str__()
        AD object with value of [1 2] and derivative of [1.0, 0.0][0.0, 1.0]
        """
        return "AD object with value of {} and derivative of {}".format(
            self.val, self.der.tolist()
        )

    def __repr__(self):
        """Returns the representation of the current AD object.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        AD: the representation of the AD object

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> x.__repr__()
        AD: [1 2], [1.0, 0.0][0.0, 1.0]
        """
        return "AD: {}, {}".format(self.val, self.der.tolist())

    def __eq__(self, other):
        """Equality method: Checks if this object is equal to another object.

        Assumes that objects are the same when values and derivatives are the same.

        INPUTS
        =======
        self: the current AD object
        other: The object we are comparing to.

        RETURNS
        ========
        True if equal, False otherwise

        EXAMPLES
        =========
        >>> x = AD(5)
        >>> y = AD(6)
        >>> x == y
        False
        """
        try:
            return np.array_equal(self.val, other.val) and np.array_equal(
                self.der, other.der
            )
        except:
            raise TypeError(
                "unsupported operand type(s) for =: {} and {}".format(
                    type(self).__name__, type(other).__name__
                )
            )

    def __ne__(self, other):
        """Inequality method: Checks if this object is not equal to another object.

        Assumes that objects are not the same when values or derivatives are not the same.

        INPUTS
        =======
        self: the current AD object
        other: The object we are comparing to.

        RETURNS
        ========
        True if not equal, False otherwise

        EXAMPLES
        =========
        >>> x = AD(5)
        >>> y = AD(6)
        >>> x != y
        True
        """
        try:
            return not (
                np.array_equal(self.val, other.val)
                and np.array_equal(self.der, other.der)
            )
        except:
            raise TypeError(
                "unsupported operand type(s) for =: {} and {}".format(
                    type(self).__name__, type(other).__name__
                )
            )

    def __neg__(self):
        """Returns the negation of the current AD object.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        AD: new instance with negation of current val, der, and ads.

        EXAMPLES
        =========
        >>> x = AD(5)
        >>> f = -x
        >>> f.val
        -5
        """
        return AD(np.negative(self.val), np.negative(self.der))

    def __pos__(self):
        """Returns the current AD object with the unary plus operator.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        AD: new instance with negation of current val, der, and ads.

        EXAMPLES
        =========
        >>> x = AD(5)
        >>> +x
        >>> f.val
        -5
        """
        return AD(self.val, self.der)

    def __abs__(self):
        """Returns the current AD object with the absolute value of val and der.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        AD: new instance with absolute values of current val, der, and ads.

        EXAMPLES
        =========
        >>> x = AD([-1, 2])
        >>> f = abs(x)
        >>> f.val[0]
        -5
        """
        return AD(np.absolute(self.val), np.absolute(self.der))

    def __add__(
        self,
    ):
        pass

    def __getitem__(self, index):
        return self.ads[index]

    def __setitem__(self, index):
        pass

    def __delitem__(self, index):
        pass

    def __iter__(self):
        """Returns an ADIterator object for the current AD object.

        INPUTS
        =======
        self: the current AD object

        RETURNS
        ========
        ADIterator: iterator object for current the AD object

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> for AD_obj in x:
        AD_obj
        """
        return ADIterator(self.ads)


class ADIterator:
    """Main object is to allow iteration over all fightingAD objects in the currect AD object.

    It returns fightingAD objects when people iterate over the currect AD object.

    Attributes
    ==========
    ads : np.array
        Array storing n different fightingAD objects representing the n variables.
    index : integer
        Variable tracking the position during the iteration.
    """

    def __init__(self, ads):
        """
        INPUTS
        =======
        values : np.array
            Array storing n different fightingAD objects to iterate over.

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> for AD_obj in x:
        AD_obj
        """
        self.index = 0
        self.ads = ads

    def __next__(self):
        """Returns the next fightingAD object in the current ADIterator object.

        INPUTS
        =======
        self: the current ADIterator object

        RETURNS
        ========
        fightingAD: next fightingAD object in the current ADIterator object

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> for AD_obj in x:
        AD_obj
        """
        try:
            next_ads = self.ads[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return next_ads

    def __iter__(self):
        """Returns the current ADIterator object.

        INPUTS
        =======
        self: the current ADIterator object

        RETURNS
        ========
        ADIterator: the current ADIterator object

        EXAMPLES
        =========
        >>> x = AD([1, 2])
        >>> for AD_obj in x:
        AD_obj
        """
        return self
