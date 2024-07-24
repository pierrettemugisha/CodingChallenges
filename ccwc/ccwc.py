#!/usr/bin/env python

import sys
import argparse
import json
import csv
import xml.etree.ElementTree as ET
import concurrent.futures
import os


def word_count(content):
    """
    Returns the number of words in the given content.

    :param content: The content to count words in.
    :return: The number of words in the content.
    """
    return len(content.decode().split())


def line_count(content):
    """
    Returns the number of lines in the given content.

    :param content: The content to count lines in.
    :return: The number of lines in the content.
    """
    return content.count(b'\n')


def byte_count(content):
    """
    Returns the number of bytes in the given content.

    :param content: The content to count bytes in.
    :return: The number of bytes in the content.
    """
    return len(content)


def character_count(content):
    """
    Returns the number of characters in the given content.

    :param content: The content to count characters in.
    :return: The number of characters in the content.
    """
    return len(content.decode())


def process_file(filename, option=None, file_type=None):
    """
    Processes a single file and prints the requested information.

    :param filename: The name of the file to process.
    :param option: The option specifying what information to print.
    :param file_type: The type of the file.
    """
    try:
        if file_type == 'json':
            with open(filename, 'r') as file:
                content = json.load(file)
                content = str(content).encode()
        elif file_type == 'csv':
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                content = str(list(reader)).encode()
        elif file_type == 'xml':
            tree = ET.parse(filename)
            root = tree.getroot()
            content = ET.tostring(root, encoding='unicode').encode()
        else:
            with open(filename, 'rb') as file:
                content = file.read()

        if option == '-c':  # byte count
            print(f'{byte_count(content)} {filename}')
        elif option == '-l':  # line count
            print(f'{line_count(content)} {filename}')
        elif option == '-w':  # word count
            print(f'{word_count(content)} {filename}')
        elif option == '-m':  # character count
            print(f'{character_count(content)} {filename}')
        elif option is None:  # no option
            print(f'{line_count(content)} {word_count(content)} {byte_count(content)} {filename}')
        else:  # invalid option
            print(f'Invalid option {option}')

    except Exception as e:
        print(f'An error occurred {e}')


def process_directory(directory, option=None, file_type=None, exclude_files=None, exclude_directories=None):
    """
    Recursively processes all files in the given directory and its subdirectories.

    :param directory: The directory to process.
    :param option: The option specifying what information to print.
    :param file_type: The type of the files.
    :param exclude_files: A list of file types to exclude.
    :param exclude_directories: A list of directory names to exclude.
    """
    for root, dirs, files in os.walk(directory):
        if exclude_directories and os.path.basename(root) in exclude_directories:
            continue
        for file in files:
            if exclude_files and file.split('.')[-1] in exclude_files:
                continue
            filename = os.path.join(root, file)
            process_file(filename, option, file_type)


def main():
    """
    The main function.
    """
    parser = argparse.ArgumentParser(prog='CustomCWTool', description="Custom Word Count Tool")
    parser.add_argument('filename', nargs='*', help='Files or directories to analyze')
    parser.add_argument('-c', '--byte-count', action='store_true', help='print the byte count')
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline count')
    parser.add_argument('-w', '--words', action='store_true', help='print the word count')
    parser.add_argument('-m', '--characters', action='store_true', help='print the character count')
    parser.add_argument('-t', '--file-type', help='specify the file type (json, csv, xml)')
    parser.add_argument('-e', '--exclude-files', help='specify file types to exclude (comma separated)')
    parser.add_argument('-d', '--exclude-directories', help='specify directory names to exclude (comma separated)')

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

    exclude_files = args.exclude_files.split(',') if args.exclude_files else None
    exclude_directories = args.exclude_directories.split(',') if args.exclude_directories else None

    if args.filename:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for filename in args.filename:
                if os.path.isdir(filename):
                    futures.append(executor.submit(process_directory, filename, option, args.file_type, exclude_files, exclude_directories))
                else:
                    futures.append(executor.submit(process_file, filename, option, args.file_type))
            for future in concurrent.futures.as_completed(futures):
                future.result()
    else:
        if sys.stdin.isatty():
            print('Error: Please provide either standard input or a filename')
        else:  # Content is passed as standard input
            content = sys.stdin.buffer.read()
            if option == '-c':  # byte count
                print(f'{byte_count(content)}')
            elif option == '-l':  # line count
                print(f'{line_count(content)}')
            elif option == '-w':  # word count
                print(f'{word_count(content)}')
            elif option == '-m':  # character count
                print(f'{character_count(content)}')
            elif option is None:  # no option
                print(f'{line_count(content)} {word_count(content)} {byte_count(content)}')
            else:  # invalid option
                print(f'Invalid option {option}')


if __name__ == "__main__":
    main()