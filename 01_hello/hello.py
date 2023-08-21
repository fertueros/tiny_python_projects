#!/usr/bin/env python3
# Say hello

import argparse


def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='World', help='Name to greet')
    args = parser.parse_args()
    name = args.name
    print(f"Hello, {name}!")


if __name__ == '__main__':
    main()
