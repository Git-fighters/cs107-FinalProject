#!/usr/bin/env python3
# Package aiming to enable automatic differentiation with Python.
# By Manana Hakobyan, Tale Lokvenec, Hugo Fernandez-Montenegro, and Golo Feige

import numpy as np 
from gitfighters.git_fighters import *

class AD:
    """Main object to handle vector functions with multiple real scalar or vector inputs.
    
    People will use this class to perform calculations on vector functions.
    It creates AD objects supporting custom operations for Automatic Differentiation.
    
    Attributes
    ==========
    values : np.array
        Array storing n different variables to evaluate.
    derivatives : np.array 
        Matrix (n x n) of derivatives. The default value is In.
    ads : np.array
        Array storing n different fightingAD objects representing the n variables.
    """   

 
    def __init__(self, values, derivatives = None):
        """
        INPUTS
        =======    
        values : np.array
            Array storing n different variables to evaluate.
        derivatives : np.array 
            Matrix (n x n) of derivatives. The default value is In. 

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
        >>> f.values
        [1 2]
        >>> f.derivatives
        [[1. 0.]
         [0. 1.]]
        """ 
        if np.array(values).shape == ():
            self.values = np.array([values])
        else:
            self.values = np.array(values) 
    
        dim = len(list(self.values))
        der_matrix = np.identity(dim) 
        self.ads = np.array([])
        
        if derivatives:
            if len(derivatives) != len(values):
                raise Exception("derivatives and values not the same shape")
            der_matrix = der_matrix * np.array(derivatives)
               
        try:
            for i in range(dim):
                der_matrix[i, i] = self.values[i].der 
                self.ads = np.append(self.ads, fightingAD(self.values[i].val, der_matrix[i, :]))
        except AttributeError:
            for i in range(dim):
                self.ads = np.append(self.ads, fightingAD(self.values[i], der_matrix[i, :]))
        self.derivatives = der_matrix


    def __add__(self, ):
        pass

    def __getitem__(self,index):
        return self.ads[index]
         
    def __setitem__(self, index):
        pass
    
    def __delitem__(self, index):
        pass
    
    def __iter__(self):
        return self

    def __next__():
        pass
