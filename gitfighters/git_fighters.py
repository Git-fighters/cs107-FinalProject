#!/usr/bin/env python3
#This package aiming to enable automatic differentiation with Python.
#By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

class fightingAD():

    #Constructor to set class up
    def __init__(self, value, derivative=1):
        self.val = value
        self.der = derivative

    #Overload str
    def __str__(self):
        return 'Function with value of {} and derivative of {}'\
               .format(self.val, self.der)

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
            raise TypeError('unsupported operand type(s) for +: {} and {}'\
                      .format(type(self).__name__, type(other).__name__)) 

    def __radd__(self, other):
        return self.__add__(other)    

    #Overload multiplication
    def __mul__(self, other):
        try:
            return fightingAD(self.val * other.val, 2 * self.val * other.der)
        except AttributeError:
            try:
                return fightingAD(self.val * other, self.der * other)
            except:
                raise TypeError('unsupported operand type(s) for *: {} and {}'\
                      .format(type(self).__name__, type(other).__name__)) 
        else:
            raise TypeError('unsupported operand type(s) for +: {} and {}'\
                      .format(type(self).__name__, type(other).__name__)) 

    def __rmul__(self, other):
        return self.__mul__(other)


#Demo code
a = 5.0
x = fightingAD(a)
alpha = 2.0
beta = 3.0

f1 = alpha * x + beta
print('f1 = alpha * x + beta | x = 5, alpha = 2, beta = 3')
print('output: val der')
print(f1.val, f1.der)

f2 = x * alpha + beta
print('f2 = x * alpha + beta | x = 5, alpha = 2, beta = 3')
print('output: val der')
print(f2.val, f2.der)

f3 = beta + alpha * x
print('f3 = beta + alpha * x | x = 5, alpha = 2, beta = 3')
print('output: val der')
print(f3.val, f3.der)

f4 = beta + x * alpha
print('f4 = beta + x + alpha | x = 5, alpha = 2, beta = 3')
print('output: val der')
print(f4.val, f4.der)

f5 = x * x
print('f5 = x * x | x = 5')
print('output: val der')
print(f5.val, f5.der)

f6 = x * x * x
print('f6 = x * x * x | x = 5')
print(f6.val, f6.der)

f7 = x + x
print('f7 = x + x | x = 5')
print(f7.val, f7.der) 
