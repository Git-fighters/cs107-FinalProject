from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
nltk.download('stopwords')
nltk.download('punkt')

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

    stop_words = np.array(stopwords.words('english')) ### get the english stipwords
    stop_words_set = set(stopwords.words('english'))  ### take out the single letters since they might be variables
    for s in stop_words:
        if len(s)==1:
            stop_words_set.remove(s)        
    stop_words_set.add('=') ### add '=' for the case when the user inputs "... where x=2, y=3"
    
    ### tokenize the user input and take out the stop words
    word_tokens = word_tokenize(user_input) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words_set]

    return filtered_sentence

def get_equation(filtered_sentence, operations):
    """ Parses and separates the equation part from the string

        INPUTS
        =======
        filtered_sentence: a list of tokenized strings from the original equation 
        operations: a pre-defined list of mathematical operations in string format

        RETURNS
        ========
        string: the equation part

        EXAMPLES
        =========
        >>> ops = ['+', '-', '**', '^', '*', '/', '|', ':', ')', '(']
        >>> filtered_sentence = parse_sentence('x^2 + 2x when x is 1')
        >>> get_equation(filtered_sentence, ops)
        >>> 'x^2 + 2x'
        
        """

    i = 0
    equation = ''

    while i < len(filtered_sentence):
    ### current expression
        expr = filtered_sentence[i]
        str_op = [op for op in operations if op in expr]

    ### next 
        if i+1 < len(filtered_sentence):
            expr_next = filtered_sentence[i+1]
            str_op_next = [op for op in operations if op in expr_next]
        else:
            expr_next = ''
            str_op_next  = ['no operation']
    ### prev
        if i-1 >= 0:
            expr_prev = filtered_sentence[i-1]
            str_op_prev = [op for op in operations if op in expr_prev]
        else:
            expr_prev = ''
            str_op_prev  = ['no operation']

        if i == 0 and len(str_op) >= 1:
            equation += expr

        elif (i > 0) and (len(expr)==1) and (len(str_op) == 1): ### second or third term
            if (len(str_op_next) == 0) and (len(str_op_prev) == 0): 
                equation += expr_prev + expr+ expr_next
        
            elif (len(str_op_next) == 0):
                equation += expr + expr_next
               
            elif (len(str_op_prev) == 0):
                equation += expr_prev + expr
              

            else:
                equation += expr            

        elif (expr[-1] in operations) and (len(str_op_next) == 0) and (len(expr) > 1):
            equation += expr + expr_next

        elif len(str_op) >= 1:
            equation += expr
        i += 1
        
    return equation


def remove_the_eq(single_eq_elements, single_filtered_elements):
""" Returns a list of tokenized strings after removing the parts belonging to the equation

        INPUTS
        =======
        single_eq_elements: a list of single string elements that constitute the equation
        single_filtered_elements: a list of single elements that constitute the user input without the stop words

        RETURNS
        ========
        list: a list of tokenized strings after removing the parts belonging to the equation

        EXAMPLES
        =========
        >>> single_eq_elements = ['x', '^', '2', '+', '2', 'x']
        >>> single_filtered_elements = ['x', '^', '2', '+', '2', 'x', 'x', '1']
        >>> remove_the_eq(single_eq_elements, single_filtered_elements)
        >>> ['x', '1']
        
        """


    first_eq_elem = single_eq_elements[0]
    last_eq_elem = single_eq_elements[-1]
    len_eq = len(single_eq_elements)

    ind_first_elem = single_filtered_elements.index(first_eq_elem)
    ind_last_elem = ind_first_elem + len_eq -1 

    if (single_filtered_elements[ind_first_elem] == first_eq_elem) and (single_filtered_elements[ind_last_elem] == last_eq_elem):
        for i in single_filtered_elements[ind_first_elem : ind_last_elem +1]:
            single_filtered_elements.remove(i)
    else:
        remove_the_eq(single_eq_elements, single_filtered_elements[1:])

    return single_filtered_elements



def get_values(variables, vars_vals):
    """ Returns a dictionary where the keys are the variable names and the values are the variable values

        INPUTS
        =======
        variables: variables that are filtered via regex from the equation
        vars_vals: the remainder of the tokenized/filtered list after removing the equation part

        RETURNS
        ========
        dictionary: the keys are the variable names and the values are the variable values

        EXAMPLES
        =========
        >>> variables = ['x']
        >>> vars_vals = ['x', '1']
        >>> get_values(variables, vars_vals)
        >>> {'x': '1'}
        
        """

    values = {}
    for item in variables:
        ind_item = vars_vals.index(item)
        if ind_item % 2 == 0:
            values[item] = vars_vals[ind_item+1]
        else:
            values[item] = vars_vals[ind_item-1]
    return values



def pythonize(eq, variables): 
    
    eq = eq.replace('^', '**')
    eq = eq.replace(':', '/')
    eq = eq.replace(',', '')
    
    varstring = ''.join(variables)
    opstring = '+-\\|\\|*\\/:\\^()'
    
    regex = f"([0-9.]+[{varstring}])"
    matches = re.findall(regex, eq)
    
    for mat in matches:
        print(mat)
        m = re.match(r"(\d+)([xy]{1})", mat)
        first = m.group(1)
        second = m.group(2)
        sub_regex = f"({first}{second})"
        eq = re.sub(sub_regex, '*'.join(m.groups()), eq)
    
    return eq

def pipeline(user_input):
    
    '''
    INPUT
    user_input: human readable sentence which asks to evaluate or differentiate the given equation at the given points
    
    OUPUTS
    eq: python readable string equation; 'eval' can be directly called to evaluate
    val_dict: the dictionary of variables and values to make the AD object with
    
    '''
    
    ### tokenize and parse the sentence
    filtered_sentence = parse_sentence(user_input)
    
    ### separate the equation from the user input
    operations = ['+', '-', '**', '^', '*', '/', '|', ':', ')', '('] ## define the operations
    eq = get_equation(filtered_sentence, operations)
    
    
    ### split all the elements in the tokenized list into single elements
    single_filtered_elements = []
    for expr in filtered_sentence:
        single_filtered_elements.extend(re.split('', expr)[1:-1])
    
    ### split the equation into single elements
    single_eq_elements = re.split('', eq)[1:-1]
    
    ### get the remainder of the tokenized list after removing the equation
    ### possibly; the variables and values
    vars_vals = remove_the_eq(single_eq_elements, single_filtered_elements)
    
    
    ### possible variables from the equation (should be processed more)
    var_regex = r"[^\d (sin) (cosin) (tan) (arctan) * \.|+-:/\^]"
    variables = re.findall( var_regex, eq)
    
    ### gets the variables and values in the dictionary format
    val_dict = get_values(variables, vars_vals)
    
    ### clean and pythonize the equation
    eq = pythonize(eq, variables)      
    
    return eq, val_dict


