# translator.py
# takes the Scheme source and builds AST in memory, then outputs Python code and makes output.py

from parser import parse
from lexer import tokenize

# converts AST nodes into Python syntax
def translate(ast):
    # handle any empty list
    if not ast:
        return "[]"

    # base case: literal or variable
    if isinstance(ast, bool):
        return "True" if ast else "False"
    if isinstance(ast, (int, float)):
        return str(ast)
    if isinstance(ast, str) and not ast.isidentifier():
        return f'"{ast}"'
    if isinstance(ast, str):
        return ast

    # arithmetic: (+ 3 2) → (3 + 2)
    if ast[0] in ['+', '-', '*', '/']:
        left = translate(ast[1])
        right = translate(ast[2])
        return f"({left} {ast[0]} {right})"

    # 'define' function: (define (square x) (* x x))
    if ast[0] == 'define':
        func_name = ast[1][0]
        args = ", ".join(ast[1][1:])
        body = translate(ast[2])
        return f"def {func_name}({args}):\n    return {body}"

    # 'display' call: (display (square 5))
    if ast[0] == 'display':
        return f"print({translate(ast[1])})"

    # quoted lists: '(1 2 3) → [1, 2, 3]
    if ast[0] == 'quote':
        quoted = ast[1]
        if isinstance(quoted, list):
            return f"[{', '.join(translate(x) for x in quoted)}]"
        else:
            return f"{translate(quoted)}"

    # 'cons' (construct lists)
    if ast[0] == 'cons':
        head = translate(ast[1])
        tail = translate(ast[2])
        if tail.startswith('['):
            return f"[{head}] + {tail}"
        else:
            return f"({head}, {tail})"

    # generic function calls: (square 5) → square(5)
    if isinstance(ast[0], str):
        func_name = ast[0]
        args = ", ".join(translate(arg) for arg in ast[1:])
        return f"{func_name}({args})"

    # unrecognized AST form
    raise ValueError(f"Unsupported AST form: {ast}")


if __name__ == "__main__":
    with open("scheme_input.scm") as f:
        code = f.read()

    tokens = tokenize(code)
    ast = parse(tokens)
    py_code = translate(ast)

    with open("output.py", "w") as out:
        out.write(py_code + "\n")

    print("[translator.py] Translation result:")
    print(py_code)