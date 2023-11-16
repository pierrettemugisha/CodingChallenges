#!/usr/bin/env python

import sys
import argparse


def wc(filename, option=None):
    try:
        with open(filename, 'rb') as file:

            content = file.read()

            if option == '-c':
                count = len(content)
            elif option == '-l':
                count = content.count(b'\n')
            else:
                print(f'Invalid option {option}')

            print(f'{count} {filename}')

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
    except Exception as e:
        print(f'An error occurred {e}')


def main():
    parser = argparse.ArgumentParser(description="Custom Word Count Tool")
    parser.add_argument('filename', help='File to analyse')
    parser.add_argument('-c', '--byte-count', action='store_true', help='print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='print the byte counts')
    args = parser.parse_args()

    if args.byte_count:
        wc(args.filename, '-c')
    elif args.lines:
        wc(args.filename, '-l')


if __name__ == "__main__":
    main()
