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
    graph_name = name + datetime.now().strftime('%Y%m%d_%H%M%S')
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    plt.savefig(f"graphs/{name}_graph.png")
    print(f"graph saved as graphs/{graph_name}_graph.png")
    return "{graph_name}_graph"


def visualize(function, variables, derivatives):
    """visualizes the automatic differentiation process

    INPUTS
    =======
    function: a callable python function
    variables: dictionary with
        keys: variable names
        values: variable values
    derivatives: dictionary with
        keys: variable names
        values: derivative values
    RETURNS
    =======
    """

    # AWAITING CLI TO DECIDE ON HOW TO DO THIS
    # 1. for each variable
    # 2. assume all other variables become constants
    # 3. modify function accordingly
    # 4. Create 1D plot by calling visualize_1D(function, value, derivative)

    i = 0
    graph_names = []
    for variable, value in variables.items():
        graph_names.append(visualize_1D(function, value, derivatives[i], name=variable))
        i += 1
        
    return graph_names
