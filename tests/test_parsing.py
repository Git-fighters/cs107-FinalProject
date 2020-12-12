from gitfighters.parsing import *
from gitfighters.git_fighters import *
from gitfighters.vector import *
import numpy as np
import pytest
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

test_strings = [
    "x^2 + y^2 when x is 1 and y is 2",
    "x when x is 1",
    "x-y where x is 1 and y is 3",
    "y^2 when y is 2",
    "exp(x) + 1 when x is 1",
    "x + y where x = 1 and y=2",
    "x + 4^x when x is 1",
    "x^2 + y- 7xy where x is 2 and y is 8",
    "sin(x) + cos(y) when x is 1 and y is 2",
    "2 + sin(x) - 3y where x=2 and y=3",
    "x + 4^x when x is 1",
    "exp(6y + 3^y) where x is 4 and y = 3",
    "sin(x) + exp(y) - 7xyz when x=2 and y=8, z=1",
    "x^2 + y^2 when x is 1 and y is 2",
    "100 ^(xy) where x = 1000, y=3",
    "x^2+y-7xy if x = 1 and y = 0",
    " x= 2 and y= 84 for y^2 + 3x + 5y",
    "x^3 + 2x + 1 where x is 1",
]


def test_parsing():
    for test_string in test_strings:
        eq, vals = pipeline(test_string)
        print("user input:", test_string)
        print("equation:", eq)
        print("variables and values:", vals)

test_parsing()


