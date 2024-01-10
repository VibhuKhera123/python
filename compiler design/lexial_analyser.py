import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0

    def get_next_token(self):
        if self.position >= len(self.source_code):
            return Token('EOF', None)

        current_char = self.source_code[self.position]
        if current_char.isspace():
            self.position += 1
            return self.get_next_token()
        if current_char.isdigit():
            return self.get_number()
        if current_char.isalpha():
            return self.get_identifier()
        if current_char == "'":
            return self.get_string_literal()
        special_characters = {'+', '-', '*', '/', '(', ')', '<', '>', '=', ':'}
        if current_char in special_characters:
            return self.get_multi_character_token()
        if current_char == ';':
            self.position += 1
            return Token('SEMICOLON', ';')
        raise Exception(f"Invalid character: {current_char}")

    def get_number(self):
        number = ""
        while self.position < len(self.source_code) and self.source_code[self.position].isdigit():
            number += self.source_code[self.position]
            self.position += 1
        return Token('INTEGER', int(number))

    def get_identifier(self):
        identifier = ""
        while self.position < len(self.source_code) and (self.source_code[self.position].isalpha() or self.source_code[self.position].isdigit()):
            identifier += self.source_code[self.position]
            self.position += 1
        keywords = {'if', 'else', 'while', 'def', 'int'}
        token_type = 'KEYWORD' if identifier in keywords else 'IDENTIFIER'
        return Token(token_type, identifier)

    def get_string_literal(self):
        self.position += 1  
        string_literal = ""

        while self.position < len(self.source_code):
            current_char = self.source_code[self.position]

            if current_char == "'":
                self.position += 1 
                return Token('STRING', string_literal)

            string_literal += current_char
            self.position += 1

        raise Exception("Unterminated string literal")

    def get_multi_character_token(self):
        current_char = self.source_code[self.position]

        if current_char == '<' or current_char == '>':
            next_char = self.source_code[self.position + 1] if self.position + 1 < len(self.source_code) else None

            if next_char == '=':
                self.position += 2
                return Token('OPERATOR', current_char + '=')
        
        self.position += 1
        return Token('OPERATOR', current_char)

if __name__ == "__main__":
    source_code = input("Enter the source code: ")
    lexer = Lexer(source_code)

    print("| Type        | Character |")
    print("|-------------|-----------|")

    while True:
        token = lexer.get_next_token()
        if token.type == 'EOF':
            break
        print(f"| {token.type:<11} | {token.value:<9} |")
    print('\n\n')

