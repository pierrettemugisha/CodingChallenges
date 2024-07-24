from jsonlexer import JSONLexer
from jsonparser import JSONParser


def main():
    json_string = '{"key": "value"}'
    lexer = JSONLexer(json_string)
    tokens = lexer.tokenize()
    parser = JSONParser(tokens)
    try:
        parsed_data = parser.parse()
        print(f'Valid JSON: {parsed_data}')
        exit(0)
    except ValueError as e:
        print(f'Invalid JSON: {e}')
        exit(1)


if __name__ == '__main__':
    main()
