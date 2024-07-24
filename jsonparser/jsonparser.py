class JSONParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        if self.tokens[self.pos] == ('LBRACE', '{') and self.tokens[self.pos + 1] == ("RBRACE", '}'):
            return {}
        else:
            raise ValueError('Invalid JSON object')
