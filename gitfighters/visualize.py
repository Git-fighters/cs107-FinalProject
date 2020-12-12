import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from gitfighters.git_fighters import *


def visualize_1D(function, value, der, name="x"):
    """creates a matplotlib plot and stores it as an image in users current directory

    INPUTS
    =======
    function: a callable python function
    value: value at which said function is evaluated
    """

    # plot function
    xs = np.linspace(value - 50, value + 50, 100)
    ys = function(xs)
    plt.plot(xs, ys)

    # plot the point at which the function is evaluated
    plt.plot(value, function(value), "r*")

    # labels
    plt.xlabel(f"{name}-axis")
    plt.ylabel("function value")
    plt.legend(
        [
            f"function value in respect to {name}",
            "value at which the function is evaluated",
        ]
    )
    text = f"der value: {der}"
    plt.text(
        value + 30,
        function(value),
        text,
        bbox=dict(fill=False, edgecolor="red", linewidth=2),
    )

    plt.show()
    filepath = "graphs/"
    graph_name = name + datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    plt.savefig(f"graphs/{graph_name}_graph.png")
    print(f"graph saved as graphs/{graph_name}_graph.png")

    # clear graph
    plt.clf()
    return f"{graph_name}_graph"


def visualize(function, variables, derivatives):
    """visualizes the automatic differentiation process
    INPUTS
    =======
    function: a mathematical python function in string format
    variables: dictionary with
        keys: variable names
        values: variable values
    derivatives: dictionary with
        keys: variable names
        values: derivative values
    RETURNS
    =======
    """
    # PSEUDOCODE
    # 1. for each variable
    # 2. assume all other variables become constants
    # 3. modify function accordingly
    # 4. Create 1D plot by calling visualize_1D(function, value, derivative)

    i = 0
    graph_names = []
    for variable, value in variables.items():

        mod_function = function
        for variable2, value2 in variables.items():
            if variable2 != variable:
                mod_function = mod_function.replace(variable2, str(value2))

        mod_function = f"""
def f({variable}):
    return {mod_function}
"""
        exec(mod_function, globals())

        graph = visualize_1D(f, value, derivatives[variable], name=variable)
        graph_names.append(graph)
        i += 1

    return graph_names
