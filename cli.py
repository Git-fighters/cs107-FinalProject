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

    ########################################################################################################
    # I DONT QUITE UNDERSTAND THE SEQUENCE OF THE PARSING NOTEBOOK, BUT IT SHOULD BE SMTH LIKE THIS
    filtered_sentence, word_tokens = parse_sentence(user_input)
    equation = get_equation(filtered_sentence, word_tokens)

    clean_equation, variables
    # now we have to execute
    exec("f = {}".format(clean_equation))

    # differentiate and evaluate
    difs = differentiate()
    vals = evaluate()
    print(f"your values are: ")
    print(vals)
    print(f"derivative values are")
    print(difs)
    #######################################################################################################

    latex_bool = input("would you like to output a latex file? Y/n")
    if latex_bool == "Y":
        # CREATE LATEX FILE
        pass
    vis_bool = input("would you like visualize your function and its derivaive? Y/n")
    if vis_bool == "Y":
        # VISUALIZE FUNCTION
        pass


if __name__ == "__main__":
    main()
