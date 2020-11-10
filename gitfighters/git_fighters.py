#!/usr/bin/env python3
#This package aiming to enable automatic differentiation with Python.
#By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

class fightingAD():

    #Constructor to set class up
    def __init__(self, value, derivative=1.0):
        self.val = value
        self.der = derivative

    #Overload str
    def __str__(self):
        return 'AD object with value of {} and derivative of {}'\
               .format(self.val, self.der)

    #Overload repr
    def __repr__(self):
        return 'AD: {}, {}'.format(self.val, self.der)

    #Overload eq
    def __eq__(self, other):
        try:
            return (self.val == other.val) and (self.der == other.der)
        except:
            raise TypeError('unsupported operand type(s) for =: {} and {}'\
                      .format(type(self).__name__, type(other).__name__))

    #Overload addition
    def __add__(self, other):
        try:
            return fightingAD(self.val + other.val, self.der + other.der)
        except AttributeError:
            try:
                return fightingAD(self.val + other, self.der)
            except:
                raise TypeError('unsupported operand type(s) for +: {} and {}'\
                      .format(type(self).__name__, type(other).__name__))      
        else:
            raise Exception('unsupported operation for +')

    #Overload addition with reversed operands
    def __radd__(self, other):
        return self.__add__(other)    

    #Overload subtraction
    def __sub__(self, other):
        try:
            return fightingAD(self.val - other.val, self.der - other.der)
        except AttributeError:
            try:
                return fightingAD(self.val - other, self.der)
            except:
                raise TypeError('unsupported operand type(s) for -: {} and {}'\
                      .format(type(self).__name__, type(other).__name__))
        else:
            raise Exception('unsupported operation for -')

    #Overload subtraction with reversed operand by negating values
    def __rsub__(self, other):
        return fightingAD(-self.val, -self.der).__add__(other)

    #Overload multiplication
    def __mul__(self, other):
        try:
            return fightingAD(self.val * other.val, \
                              self.val * other.der + self.der * other.value)
        except AttributeError:
            try:
                return fightingAD(self.val * other, self.der * other)
            except:
                raise TypeError('unsupported operand type(s) for *: {} and {}'\
                      .format(type(self).__name__, type(other).__name__)) 
        else:
            raise Exception('unsupported operation for *') 

    #Overload multiplication with reversed operand
    def __rmul__(self, other):
        return self.__mul__(other)

    #Overload division
    def __div__(self, other):
        try:
            if other.val == 0:
                raise ZeroDivisionError('division by zero')
            return fightingAD(self.val / other.val,\
                             (self.der * other.val - self.val * other.der) / \
                             (other.val * other.val)) 
        except AttributeError:
            try:            
                return fightingAD(self.val / other, self.der / other)
            except:
                raise TypeError('unsupported operand type(s) for /: {} and {}'\
                      .format(type(self).__name__, type(other).__name__))
        else:
            raise Exception('unsupported operation for /')
   
    #Overload division with reversed operand
    def __rdiv__(self, other):
        try:
            return fightingAD(other).__div__(self)
        except:
            raise Exception('unsupported operation for /')

