import matplotlib.pyplot as plt
import numpy as np
import os


def visualize_1D(function, value, der, name="x"):
    """creates a matplotlib plot and stores it as an image in users current directory

    INPUTS
    =======
    function: a callable python function
    value: value at which said function is evaluated
    """

    # plot temperature curve
    xs = np.linspace(value - 50, value + 50, 100)
    ys = function(xs)
    plt.plot(xs, ys)

    # plot horizontal line
    # xs = np.linspace(0,20,100)
    # ys = np.full(100, 45)
    # plt.plot(xs, ys, 'r')

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
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    plt.savefig(f"graphs/{name}_graph.png")
    print(f"graph saved as graphs/{name}_graph.png")


def visualize(function, variables, derivatives):
    """visualizes the automatic differentiation process

    INPUTS
    =======
    function: a callable python function
    variables: dictionary with
        keys: variable names
        values: variable values
    RETURNS
    =======
    n 1D graphs are created as follows:
    x + y, x = 5, y = 6
    y: assume x = val
    f1 = 5 + y
    f2 = x + 6
    ...
    """


#     # We creat a plot for each variable
#     for i, var in enumerate(variables):
#         # determine the x range
#     var = float(var)

#     xs = np.linspace(var-50,var+50,100)
#     # define the function
#     if isinstance(function, string):
#         pass
#         # def function:


#     else:  # we assume it's a function and therefore callable
#         ys = function(xs)
