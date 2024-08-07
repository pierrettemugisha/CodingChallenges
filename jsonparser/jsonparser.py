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
                    if self.tokens[self.pos][0] == 'STRING':
                        value = self.tokens[self.pos][1][1:-1]
                        obj[key] = value
                        self.pos += 1
                        if self.tokens[self.pos] == ('COMMA', ','):
                            self.pos += 1
                        elif self.tokens[self.pos] == ('RBRACE', '}'):
                            break
                        else:
                            raise ValueError('Expected comma or closing brace')
                    else:
                        raise ValueError('Expected string value')
                else:
                    raise ValueError('Expected colon')
            else:
                raise ValueError('Expected string key')
        return obj
