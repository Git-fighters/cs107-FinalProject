from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def parse_sentence(user_input):
    stop_words = np.array(stopwords.words("english"))
    stop_words_set = set(stopwords.words("english"))
    for s in stop_words:
        if len(s) == 1:
            stop_words_set.remove(s)
    stop_words_set.add("=")

    word_tokens = word_tokenize(user_input)
    filtered_sentence = [w for w in word_tokens if not w in stop_words_set]
    return filtered_sentence, word_tokens


def get_equation(filtered_sentence, operations):

    i = 0
    equation = ""

    while i < len(filtered_sentence):
        ### current expression
        expr = filtered_sentence[i]
        str_op = [op for op in operations if op in expr]
        ### next
        if i + 1 < len(filtered_sentence):
            expr_next = filtered_sentence[i + 1]
            str_op_next = [op for op in operations if op in expr_next]
        else:
            expr_next = ""
            str_op_next = ["no operation"]

        if i - 1 >= 0:
            expr_prev = filtered_sentence[i - 1]
            str_op_prev = [op for op in operations if op in expr_prev]
        else:
            expr_prev = ""
            str_op_prev = ["no operation"]

        if i == 0 and len(str_op) >= 1:
            equation += expr
            print("case 1", equation)

        elif i > 0 and len(str_op) == 1:  ### second or third term
            if (len(str_op_next) == 0) and (len(str_op_prev) == 0):
                equation += expr_prev + expr + expr_next
                print("case 2.1", equation)
            elif len(str_op_next) == 0:
                equation += expr + expr_next
                print("case 2.2", equation)
            elif len(str_op_prev) == 0:
                equation += expr_prev + expr
                print("case 2.3", equation)

            else:
                equation += expr
                print("case 2.4", equation)
            print("case 2", equation)

        elif (expr[-1] in operations) and (len(str_op_next) == 0) and (len(expr) > 1):
            equation += expr + expr_next

            print("case 3", equation)

        elif len(str_op) >= 1:
            equation += expr
            print("case 4", equation)

        i += 1

    return equation


def get_values(set_variables, vars_vals):
    values = {}
    for item in set_variables:
        ind_item = vars_vals.index(item)
        if ind_item % 2 == 0:
            values[item] = vars_vals[ind_item + 1]
        else:
            values[item] = vars_vals[ind_item - 1]
    return values
