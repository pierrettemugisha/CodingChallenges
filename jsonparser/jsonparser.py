class JSONLexer:
    def __init__(self, input_string):
        self.sinput = input_string
        self.pos = 0

    def get_next_token(self):
        while self.pos < len(self.sinput):
            current_char = self.sinput[self.pos]

            if current_char.isspace():
                self.pos += 1
                continue
            elif current_char == '{':
                self.pos += 1
                return {'type': 'LBRACE', 'value': '{'}
            elif current_char == '}':
                self.pos += 1
                return {'type': 'RBRACE', 'value': '}'}
            else:
                self.pos += 1
                raise ValueError(f'Invalid character: {current_char}')

        return {'type': 'EOF', 'value': None}


class JSONParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def parser(self):
        if self.current_token['type'] == 'LBRACE':
            self.eat('LBRACE')
            self.eat('RBRACE')
            print(f'Valid JSON')
            exit(0)
        else:
            print(f'Invalid JSON')
            exit(1)

    def eat(self, token_type):
        if self.current_token['type'] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f'Expected {token_type}, got {self.current_token['type']}')


def json_parser(input_string):
    try:
        lexer = JSONLexer(input_string)
        parser = JSONParser(lexer)
        parser.parser()
    except Exception as ex:
        print(f'An error occurred: {ex}')


def main():
    json_parser('{')


if __name__ == "__main__":
    main()
