from lexer import lexer

def parse(tokens):
    # no tokens left? (empty input)
    if not tokens:
        # the input ended before parsing finished
        raise SyntaxError("Unexpected EOF")

    # get the first token and (remove it from the list)
    token_type, token_value = tokens.pop(0)

    # if we hit a left parenthesis, start a new expression list
    if token_type == 'LPAREN':
        expr = []
        # keep parsing -> right parenthesis
        while tokens[0][0] != 'RPAREN':
            # recursive call for nested parts
            expr.append(parse(tokens))
        # remove the closing parenthesis
        tokens.pop(0)
        return expr

    # if it finds a right parenthesis without a matching left one = error
    elif token_type == 'RPAREN':
        raise SyntaxError("Unexpected RPAREN")

    # if a # token, convert it to an int or float
    elif token_type == 'NUMBER':
        return float(token_value) if '.' in token_value else int(token_value)

    # return raw value for string tokens
    elif token_type == 'STRING':
        return token_value
    
    # convert Scheme #t/#f to True/False
    elif token_type == 'BOOL':
        return True if token_value == '#t' else False

    # literal 'x = ['quote', 'x']
    elif token_type == 'QUOTE':
        # parse next expression AFTER the quote
        quoted_expr = parse(tokens)
        return ['quote', quoted_expr]
    
    # return symbol tokens (operators, variable names, etc.)
    elif token_type == 'SYMBOL':
        return token_value

    # else unexpected = invalid token type
    else:
        raise SyntaxError(f"Unknown token type: {token_type}")

if __name__ == "__main__":
    # open/read source file (scheme)
    with open("scheme_input.scm") as f:
        code = f.read()

    # tokenize the Scheme code
    tokens = lexer(code)

    # parse all expressions
    ast_list = []
    while tokens:
        ast_list.append(parse(tokens))

    # Display
    print("[parser.py] AST Output:")
    for ast in ast_list:
        print(ast)