#!/usr/bin/env python

###########################
# CLI SKELETON
###########################

from gitfighters.git_fighters import *
from gitfighters.vector import *
from gitfighters.parsing import *
from gitfighters.latex import *
from gitfighters.visualize import *


def main():
    """
    This function acts as a command line interface. User enters a function and position(s)
    they want to evaluate it at. Then:

    Then we do the following steps:
    # 1. Separate into equation string and variables string
    # 2. Clean equation and turn into python ready code (e.g. substitute ^ with **)
    # 3. Determine how many variables and what value each of these variables has
    # 4. Create a fightingAD object for each variable
    # 5. use python exec()
    # 6. print values, derivatives
    # 7. optionally output LaTeX, graphs
    """

    prompt = "Please provide a function and corresponding point(s) at which to evaluate it. \n\
EXAMPLE:   'x^2 - e^(y-1) when x=2 and y=5'\n"
    user_input = input(prompt)

    graph_names = ""
    
    while(True):
        try:
            eq, vals = pipeline(user_input)
            break
        except:
            user_input = input(f'Format not acceptable. Please change your variables/function and try again.\n')


    vect = AD(list(vals.values()))
    for key, val in vals.items():
        values = list(vals.values())
        ind = values.index(val)
        ad = vect[ind]
        globals()[f"{key}"] = ad

    exec(f"global f; f = {eq}")

    derivatives = differentiate(f)
    values = evaluate(f)
    derivatives_dict = {key: derivatives[i] for i, key in enumerate(vals)}
    print("\nWe have evaluated your function! These are the derivative values:")
    for variable, value in derivatives_dict.items():
        print(f'{variable}: {value}')
    
    
    vis_bool = input(
        "    -->Would you like visualize your function and its derivative? Y/n \n"
    )
    if vis_bool == "Y" or vis_bool == "y":
        graph_names = visualize(eq, vals, derivatives_dict)

    latex_bool = input(
        "    -->Would you like to output a nicely formatted latex file? Y/n \n"
    )
    if latex_bool == "Y" or latex_bool == "y":
        create_latex_file(derivatives, graph_names)


if __name__ == "__main__":
    main()
