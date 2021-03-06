# Math-Expression-Interpreter

A simple interpreter for evaluating mathematical expressions.

Instruction:
- Run python main.py to start the program
- Enter a mathematical expression for evaluation. For example, 3 + 5, 2 / 6, (1 + 3 * 5) / 7, etc.
- Unit tests are available for the lexer, parser and the interpreter.
  + For the lexer: run python -m unittest lexer_test.py
  + For the parser: run python -m unittest parser_test.py
  + For the interpreter: run python -m unittest interpreter.py

The lexer tokenizes the input to numbers, operators and ignores whitespaces. The parser builds an AST (Abstract Syntax Tree) from the list of tokens generated from the lexer. The interpreter evaluates the AST generated by the parser. 
