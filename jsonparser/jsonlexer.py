import re


class JSONLexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.token_specification = [
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('STRING', r'"(\\.|[^"\\])*"'),
            ('COLON', r':'),
            ('COMMA', r','),
            ('WHITESPACE', r'\s+'),
        ]
        self.token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)

    def tokenize(self):
        get_token = re.compile(self.token_regex).match
        pos = 0
        tokens = []
        while pos < len(self.input_string):
            mo = get_token(self.input_string, pos)
            if not mo:
                raise ValueError(f'Unexpected character at position {pos}')
            kind = mo.lastgroup
            if kind != 'WHITESPACE':
                tokens.append((kind, mo.group(kind)))
            pos = mo.end()
        tokens.append(('EOF', None))

        return tokens
