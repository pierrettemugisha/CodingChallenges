class JSONParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        if self.tokens[self.pos] == ('LBRACE', '{'):
            self.pos += 1
            obj = self.object()
            if self.tokens[self.pos] == ("RBRACE", '}'):
                return obj

        raise ValueError('Invalid JSON object')

    def object(self):
        obj = {}
        while self.tokens[self.pos] != ('RBRACE', '}'):
            if self.tokens[self.pos][0] == 'STRING':
                key = self.tokens[self.pos][1][1:-1]
                self.pos += 1
                if self.tokens[self.pos] == ('COLON', ':'):
                    self.pos += 1
                    value = self.value()
                    obj[key] = value
                    if self.tokens[self.pos] == ('COMMA', ','):
                        self.pos += 1
                    elif self.tokens[self.pos] == ('RBRACE', '}'):
                        break
                    else:
                        raise ValueError('Expected comma or closing brace')
                else:
                    raise ValueError('Expected colon')
            else:
                raise ValueError('Expected string key')
        return obj

    def value(self):
        token, value = self.tokens[self.pos]
        if token == 'STRING':
            self.pos += 1
            return value[1:-1]
        elif token == 'NUMBER':
            self.pos += 1
            if '.' in value or 'e' in value or 'E' in value:
                return float(value)
            return int(value)
        elif token == 'TRUE':
            self.pos += 1
            return True
        elif token == 'FALSE':
            self.pos += 1
            return False
        elif token == 'NULL':
            self.pos += 1
            return None
        else:
            raise ValueError(f'Unexpected token: {token}')
