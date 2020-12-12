###########################
# CLI SKELETON
###########################

from gitfighters.git_fighters import *
from gitfighters.vector import *
from gitfighters.parsing import *
from gitfighters.latex import *
from gitfighters.visualize import *


def main():
    prompt = "Please provide a function and corresponding point(s) at which to evaluate it. \n\
EXAMPLE:   'x^2 - e^(y-1) when x=2 and y=5'\n"
    user_input = input(prompt)

    # STEPS TO DO

    # 1. Separate into equation string and variables string
    # 2. Clean equation and turn into python ready code (e.g. substitute ^ with **)
    # 3. Determine how many variables and what value each of these variables has
    # 4. Create a fightingAD object for each variable
    # 5. execute: ('f = {}'.format(clean_equation))
    # 6. print values, derivatives

    # vis_bool = input("Do you want to give a seed? Y/n")
    # if vis_bool == "Y":
    #     # VISUALIZE FUNCTION
    #     pass

    eq, vals = pipeline(user_input)
    vect = AD(list(vals.values()))
    for key, val in vals.items():
        values = list(vals.values())
        ind = values.index(val)
        ad = vect[ind]
        globals()[f"{key}"] = ad

    exec(f"global f; f = {eq}")

    derivatives = differentiate(f)
    values = evaluate(f)
    print("\nWe have evaluated your function! These are the derivative values:")
    print(derivatives)

    vis_bool = input(
        "    -->Would you like visualize your function and its derivative? Y/n \n"
    )
    if vis_bool == "Y":
        print(eq)
        print(vals)
        print(derivatives)
        visualize(eq, vals, derivatives)

    latex_bool = input(
        "    -->Would you like to output a nicely formatted latex file? Y/n \n"
    )
    if latex_bool == "Y":
        # CREATE LATEX FILE
        print("NOT YET IMPLEMENTED")
        pass


if __name__ == "__main__":
    main()
