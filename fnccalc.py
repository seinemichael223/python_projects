#!/usr/bin/env python3

import argparse
import sys
from functools import reduce
import operator

def main():
    parser = argparse.ArgumentParser(description='Perform calculations based on the provided flag and numbers.')
    
    # Define mutually exclusive group for flags
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', action='store_true', help='Sum the numbers')
    group.add_argument('-m', '--multiply', action='store_true', help='Multiply the numbers')
    group.add_argument('-d', '--divide', action='store_true', help='Divide the first number by the second')
    
    # Positional argument for numbers
    parser.add_argument('numbers', nargs='+', type=float, help='Numbers for the calculation')
    
    args = parser.parse_args()
    
    if args.add:
        result = sum(args.numbers)
        print(f'The sum is: {result}')
    elif args.multiply:
        result = reduce(operator.mul, args.numbers, 1)
        print(f'The product is: {result}')
    elif args.divide:
        if len(args.numbers) != 2:
            print('Error: Division requires exactly two numbers.', file=sys.stderr)
            sys.exit(1)
        result = args.numbers[0] / args.numbers[1]
        print(f'The division result is: {result}')
    else:
        print('Invalid flag provided.', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

