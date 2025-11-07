# CS396_Final_Project

This project reads Scheme source code, tokenizes it, then it builds an Abstract Syntax Tree (AST) in memory, and then translates it into equivalent Python code. Demonstrating how two different programming paradigms (functional and imperative/OOP) can interoperate.

# Members:
     Christian Lamb
     McKay Hartman

# What each file does:

| File               | Description                       |
| ------------------ | ----------------------------------|
| `lexer.py`         | Tokenizes the Scheme source       |
| `parser.py`        | Builds the AST from tokens        |
| `translator.py`    | Translates AST to Python code     |
| `scheme_input.scm` | Sample Scheme input file          |

# Supports

Arithmetic: + - * /

Function definitions: (define (square x) (* x x))

Function calls: (square 5)

Boolean: #t, #f

Strings: "hello"

Quoted lists: '(1 2 3)

List construction: (cons 1 '(2 3)) → [1] + [2, 3]

Display statements: (display ...)
