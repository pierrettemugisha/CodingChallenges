class JSONLexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.position = 0

    def get_next_token(self):
        while self.position < len(self.input_string):
            current_char = self.input_string[self.position]

            if current_char.isspace():
                self.position += 1
                continue
            elif current_char == '{':
                self.position += 1
                return {'type': 'LBRACE', 'value': '{'}
            elif current_char == '}':
                self.position += 1
                return {'type': 'RBRACE', 'value': '}'}
            else:
                raise ValueError(f'Invalid character: {current_char}')
                self.position += 1

        return {'type': 'EOF', 'value': None}


class JSONParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def parse(self):
        if self.current_token['type'] == 'LBRACE':
            self.eat('LBRACE')
            self.eat('RBRACE')
            print(f'Valid JSON')
            # exit(0)
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
        parser.parse()
    except Exception as ex:
        print(f'An error occurred: {ex}')


def main():
    valid_json = '{}'
    invalid_json = '{'

    print("Parsing valid JSON:")
    json_parser(valid_json)

    print("\nParsing invalid JSON:")
    json_parser(invalid_json)


if __name__ == "__main__":
    main()
