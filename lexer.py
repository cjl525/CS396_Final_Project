# turns raw code into tokenized list of things that were separated with spaces
def tokenize(code):
    # replacing all '(' with ' ( ' and ')' with ' ) '
    code = code.replace('(', ' ( ').replace(')', ' ) ')
    tokens = code.split()
    print(tokens)




# Classifier Functions:
# These functions are able to check and return #t or #f if an
# item is a specific token

def is_lparen(token):
    return token == '('

def is_rparen(token):
    return token == ')'

def is_boolean(token):
    return token in ('#t', '#f')

def is_string(token):
    return token.startswith('"') and token.endswith('"')

def is_number(token):
    try:
        int(token)
        return True
    except ValueError:
        try:
        float(token)
        return True
    except ValueError:
        return False

def is_quote(token):
    return token =="'"

def is_symbol(token):
    return not (is_lparen(token) or is_rparen(token) or
                is_boolean(token) or is_string(token) or
                is_number(token) or is_quote(token))


# General Classifier:
# Can be used on tokens to return a tuple (''TYPE', token)
def classify_token(token):
    if is_lparen(token):
        return ('LPAREN', token)
    elif is_rparen(token):
        return ('RPAREN', token)
    elif is_boolean(token):
        return ('BOOL', token)
    elif is_string(token):
        return ('STRING', token)
    elif is_number(token):
        return ('NUMBER', token)
    elif is_quote(token):
        return ('QUOTE', token)
    else:
        return ('SYMBOL', token)



# Lexer
# Function to be used in parser.py to get the list of tuples to make ast trees
def lexer(code)
    #remove comments
    code = "\n".join(line.split(';')[0] for line in code.splitlines())
    # split into a list
    tokenized_code_list = tokenize(code)
    # classify everything into list 'tokens_list'
    tokens_list = [classify_token(individual_token) for individual_token in tokenized_code_list]
    # tokenized_list is a list of tuples
    return tokenized_list
