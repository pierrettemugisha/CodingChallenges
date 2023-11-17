#!/usr/bin/env python

import sys
import argparse


def wc(filename, option=None):
    try:
        with open(filename, 'rb') as file:

            content = file.read()

            byte_count = len(content)
            lines_count = content.count(b'\n')
            word_count = len(content.decode().split())
            character_count = len(content.decode())

            if option == '-c':  # byte count
                print(f'{byte_count} {filename}')
            elif option == '-l':  # line count
                print(f'{lines_count} {filename}')
            elif option == '-w':  # word count
                print(f'{word_count} {filename}')
            elif option == '-m':  # characters count
                print(f'{character_count} {filename}')
            elif option is None:  # no option
                print(f'{lines_count} {word_count} {byte_count} {filename}')
            else:  # invalid option
                print(f'Invalid option {option}')

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
    except Exception as e:
        print(f'An error occurred {e}')


def main():
    parser = argparse.ArgumentParser(description="Custom Word Count Tool")
    parser.add_argument('filename', help='File to analyse')
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

    wc(args.filename, option)


if __name__ == "__main__":
    main()
