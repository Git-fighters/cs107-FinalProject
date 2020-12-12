from gitfighters.parsing import *

test_strings = [
    "x^2 + y^2 when x is 1 and y is 2",
    "x when x is 1",
    "y^2 when y is 2",
    "exp(x) + 1 when x is 1",
    "x + y where x = 1 and y=2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
    "x^2 + y^2 when x is 1 and y is 2",
]


def test_parsing():
    for test_string in test_strings:
        eq, vals = pipeline(test_string)
        # try:
        #     eq, vals = pipeline(test_string)
        # except Exception as e:
        #     print(f"String: '''''{test_string}''''' failed with error:")
        #     print(e)


def test_single_input():
    test_string = ("x when x is 1",)
    eq, vals = pipeline(test_string)
