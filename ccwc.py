#!/usr/bin/env python

import sys
import argparse


def wc(filename, counts):
    try:
        with open(filename, 'rb') as file:

            content = file.read()

            if counts:
                count = len(content)
            else:
                print(f'Invalid option')

            print(f'{count} {filename}')

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
    except Exception as e:
        print(f'An error occurred {e}')


def main():
    parser = argparse.ArgumentParser(description="Custom Word Count Tool")
    parser.add_argument('filename', help='File to analyse')
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
    args = parser.parse_args()

    if args.bytes:
        wc(args.filename, '-c')


if __name__ == "__main__":
    main()
