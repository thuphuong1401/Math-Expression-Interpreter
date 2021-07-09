# Lexer: tokenizer. Decides which token ends where and its value


from lexer import Lexer

while True:
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(type(tokens))
    print(list(tokens))