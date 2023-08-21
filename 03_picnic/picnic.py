#!/usr/bin/env python3

import argparse


def main():
    """
    Programa que cambia según la palabra que se encuentra en el argumento
    """
    parser = argparse.ArgumentParser(description='hello')
    parser.add_argument('items', nargs='+', help='List of items')
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort items')
    args = parser.parse_args()
    items = args.items

    if args.sorted:
        items.sort()

    if len(items) == 1:
        print(f"You are bringing {items[0]}.")
    elif len(items) == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        items_str = ", ".join(items[:-1])
        items_str += f", and {items[-1]}"
        print(f"You are bringing {items_str}.")


if __name__ == '__main__':
    main()
