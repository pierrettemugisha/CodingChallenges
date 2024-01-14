#!/usr/bin/env python

import sys
import argparse


def wc(content, filename=None, option=None):
    try:
        byte_count = len(content)
        lines_count = content.count(b'\n')
        word_count = len(content.decode().split()) if filename else len(content.split())
        character_count = len(content.decode()) if filename else len(content)

        if option == '-c':  # byte count
            print(f'{byte_count} {filename}' if filename else f'{byte_count}')
        elif option == '-l':  # line count
            print(f'{lines_count} {filename}' if filename else f'{lines_count}')
        elif option == '-w':  # word count
            print(f'{word_count} {filename}' if filename else f'{word_count}')
        elif option == '-m':  # characters count
            print(f'{character_count} {filename}' if filename else f'{character_count}')
        elif option is None:  # no option
            print(f'{lines_count} {word_count} {byte_count} {filename}' if filename else f'{lines_count} {word_count} {byte_count}')
        else:  # invalid option
            print(f'Invalid option {option}')

    except Exception as e:
        print(f'An error occurred {e}')


def main():
    parser = argparse.ArgumentParser(prog='CodingChallenges', description="Custom Word Count Tool")
    parser.add_argument('filename', nargs='?', help='File to analyse')
    parser.add_argument('-c', '--byte-count', action='store_true', help='print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
    parser.add_argument('-m', '--characters', action='store_true', help='print the character counts')

    args = parser.parse_args()

    option = None

    if args.byte_count:
        option = '-c'
    elif args.lines:
        option = '-l'
    elif args.words:
        option = '-w'
    elif args.characters:
        option = '-m'

    if sys.stdin.isatty():
        if args.filename:  # Content is passed as a file
            try:
                with open(args.filename, 'rb') as file:
                    content = file.read()
                    wc(content, args.filename, option)
            except FileNotFoundError:
                print(f'Error: File {args.filename} not found')

        else:
            print('Error: Please provide either a standard input or a filename')
    else:  # Content is passed as standard input
        content = sys.stdin.buffer.read()
        wc(content, args.filename, option)


if __name__ == "__main__":
    main()
