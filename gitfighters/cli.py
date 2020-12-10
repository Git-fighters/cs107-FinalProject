###########################
# CLI SKELETON
###########################

# from gitfighters.git_fighters import *
# from gitfighters.vector import AD, evaluate, differentiate
# from gitfighters.parsing import *

def main():
    prompt = "Please provide a function and corresponding point(s) at which to evaluate it. \n\
EXAMPLE:   'x^2 - e^(y-1) when x=2 and y=5'\n"
    user_input = input(prompt)
    filtered_sentence, word_tokens = parse_sentence(user_input)
    equation = get_equation(filtered_sentence, word_tokens)
    
    # now we have to execute
    exec(equation)

    # differentiate and evaluate
    differentiate()
    evaluate()

    print(f'you values are:')
    

if __name__ == '__main__':
    main()