#!/usr/bin/env python3

import argparse


def main():
    """
    Programa que cambia segun la palabra que se encuentra en el argumento
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', help='Name to greet')
    args = parser.parse_args()
    name = args.name

    word = 'an' if name[0].lower() in 'aeiou' else 'a'

    print(f"Ahoy, Captain, {word} {name} off the larboard bow!")


if __name__ == '__main__':
    main()