from gitfighters.visualize import *
from cli import main


def test_visualize_1D():
    def f(x):
        return x

    visualize_1D(f, 5, 6, name="x")

def test_visualize():
    f = "x + y"
    variables = {'x':3.0, 'y':1.0}
    derivatives = {'x':1.0, 'y':1.0}
    visualize(f, variables, derivatives)