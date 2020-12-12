import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import numpy as np

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import numpy as np

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)


def parse_sentence(user_input):
    """Tokenizes the user_input, gets rid of the stop words and returns a list of tokenized string parts.

    INPUTS
    =======
    user_input: a string which typically includes some form of equation, variables and values

    RETURNS
    ========
    list: a list of tokenized parts of the sentence

    EXAMPLES
    =========
    >>> parse_sentence('x^2 + 2x when x is 1')
    >>> ['x^2', '+', '2x', 'x', '1']

    """

    stop_words = np.array(stopwords.words("english"))  ### get the english stipwords
    stop_words_set = set(
        stopwords.words("english")
    )  ### take out the single letters since they might be variables
    for s in stop_words:
        if len(s) == 1:
            stop_words_set.remove(s)
    stop_words_set.add(
        "="
    )  ### add '=' for the case when the user inputs "... where x=2, y=3"

    ### tokenize the user input and take out the stop words
    word_tokens = word_tokenize(user_input)
    filtered_sentence = [w for w in word_tokens if not w in stop_words_set]
  

    return filtered_sentence

def flatten(l):
    """This function takes a list and flattens it if there are any other list elements in it

    INPUTS
    =======
    l: any list

    RETURNS
    ========
    list: flattened list
    

    EXAMPLES
    =========
    >>> flatten(['2', '+', 'sin', '(', 'x', ')', '-', '3y', ['x', '2'], ['y', '3']])
    >>> ['2', '+', 'sin', '(', 'x', ')', '-', '3y', 'x', '2', 'y', '3']

    """ 
    
    flattened = []
    for x in l:
        if isinstance(x, list):
            flattened.extend(x)
        else:
            flattened.append(x)
    
    return flattened

def no_unwanted_symbols(filtered_sentence):
    """Cleans the string further. Gets rid of equal signs and some unneccessary punctuation.

    INPUTS
    =======
    filtered_sentence: a list of tokenized parts of the user input

    RETURNS
    ========
    list: a list of tokenized parts of the sentence but all cleaned

    EXAMPLES
    =========
    >>> no_unwanted_symbols('x^2 + 2x - 3y when x= 1, y=3')
    >>> ['x^2', '+', '2x', '-', '3y', 'x', '1', 'y', '3']

    """
    
    for i in range(len(filtered_sentence)):
        
        a = filtered_sentence[i]
        ## get rid of comma
        filtered_sentence[i] = a.replace(',', '')

        ## take out the equal signs
        if '=' in a:
            splitted = a.split('=')
            filtered_sentence[i] = splitted
            
    ## make sure there are no empty strings left in the list
    
    filtered_sentence = [i for i in filtered_sentence if i != '']
    filtered_sentence = flatten(filtered_sentence)

    return filtered_sentence

def get_variables(filtered_sentence):
    """Inspects the tokenized list and finds the variables.

    INPUTS
    =======
    filtered_sentence: a list of tokenized parts of the user input

    RETURNS
    ========
    list: a list of variables
    string: the unclean equation, essentially, the version of the first input without the stop words and all joined

    EXAMPLES
    =========
    >>> get_variables(['x^2', '+', '2x', '-', '3y', 'x', '1', 'y', '3'])
    >>> (['x', 'y'], 'x^2+2x-3yx1y3')

    """

    letter_ops = ['sin', 'cos', 'e', 'exp', 'tan', 'arctan', 'arcsin', 'arccos']
    filtered_sent_copy = filtered_sentence.copy()
    for i in letter_ops:
        if i in filtered_sent_copy:
            filtered_sent_copy.remove(i)
    unclean_eq = "".join(filtered_sent_copy)
    var_regex = r"[^\d  * \.|+-:/\^ \\( \\ )=]"
    variables = np.unique(re.findall( var_regex, unclean_eq))

    return variables, unclean_eq


def get_eq_and_vals(filtered_sentence, variables, unclean_eq):
    """Parses and separates the equation part from the values in the string

    INPUTS
    =======
    filtered_sentence: a list of tokenized strings from the original equation
    variables: list of the user defined variables
    unclean_eq: essentially the version of the first input without stop the words

    RETURNS
    ========
    string: the equation part
    list: the variables and the values in the list

    EXAMPLES
    =========  
    >>> filtered_sentence = parse_sentence('x^2 + 2x when x is 1')
    >>> get_eq_and_vals(filtered_sentence, ['x', 'y'], 'x^2+2xx1')
    >>> ('x^2 + 2x', ['x', '1'])

    """
    regex_vars = ''
    for var in variables:
        regex_vars += var + '\d+\.*\d*'
        

    var_val_str = re.findall(regex_vars,unclean_eq)[0] 
    print('vvs', var_val_str)
    values = [i for i in re.findall('\d*\.*\d*', var_val_str) if i !='']
    print('vars_vals', values)
    equation = ''
    final_eq = ''.join(filtered_sentence)
    for i in final_eq.split(var_val_str):
        if i != '':
            equation = i
    
    return equation, values



def get_values(variables, vars_vals):
    """Returns a dictionary where the keys are the variable names and the values are the variable values

    INPUTS
    =======
    variables: variables that are filtered via regex from the equation
    vars_vals: the values filtered from the input

    RETURNS
    ========
    dictionary: the keys are the variable names and the values are the variable values

    EXAMPLES
    =========
    >>> variables = ['x']
    >>> vars_vals = ['1']
    >>> get_values(variables, vars_vals)
    >>> {'x': '1'}

    """

    values = {}
    variables_list = list(variables)
    for item in variables_list:
        ind_item = variables_list.index(item)
        values[item] = float(vars_vals[ind_item])
      
    return values

def split(word):
    """This function takes a string and returns its single characters in the list

    INPUTS
    =======
    word: any string

    RETURNS
    ========
    list: a list of the characters of the word
    

    EXAMPLES
    =========
    >>> split('word')
    >>> ['w', 'o', 'r', 'd']

    """ 
    return [char for char in word]


def pythonize(eq, variables):
    """Takes in the equation part of the string and converts everything to python executable format

    INPUTS
    =======
    eq: the equation part of the user defined string
    variables: a list of variable names

    RETURNS
    ========
    string: pythonic equation

    EXAMPLES
    =========
    >>> pythonize('2^y + sin(7x)', ['x', 'y'])
    >>> '2**y + sin(7*x)'

    """ 
    
    ### take care of the exponents
    if 'e^' in eq:
        eq = eq.replace('e' , 'np.e')
        
    ### take care of division, power
    eq = eq.replace('^', '**')
    eq = eq.replace(':', '/')
    eq = eq.replace(',', '')
    

    ### take care of the multiplication (ex: xy, 7y, 6xz)
    varstring = ''.join(variables)
    opstring = '+-\\|\\|*\/:\\^' 
    
    regex = f"([0-9.]*[{varstring}]+)"
    matches = re.findall(regex, eq)
    
    for mat in np.unique(matches):
        if len(mat)>1:
            
            splitted = split(mat)
            correct_expr = '*'.join(splitted)
        
            eq = re.sub(mat, correct_expr, eq)
    
    return eq



def pipeline(user_input):
    
    """This function takes care of the whole parsing pipeline

    INPUTS
    =======
    user_input: a string which typically includes some form of equation, variables and values

    RETURNS
    ========
    string: final clean pythonic equation
    dictionary: the keys are the variable names and the values are the variable values

    EXAMPLES
    =========
    >>> pipeline('x^2 + y- 7xy where x is 2 and y is 8')
    >>> ('x**2+y-7*x*y', {'x': '2', 'y': '8'})

    """ 
    
    ### tokenize and parse the sentence
    filtered_sentence = parse_sentence(user_input)
    filtered_sentence = no_unwanted_symbols(filtered_sentence)
    
    #get the variables and the unclean equation 
    variables, unclean_eq = get_variables(filtered_sentence)
    #clean the equation and get the values for the variables
    equation, vars_vals = get_eq_and_vals(filtered_sentence, variables, unclean_eq)
 
    ### gets the variables and values in the dictionary format
    val_dict = get_values(variables, vars_vals)
    
    ### clean and pythonize the equation
    eq = pythonize(equation, variables)      
    
    return eq, val_dict


