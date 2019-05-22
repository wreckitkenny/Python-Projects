#!/usr/bin/env python
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Calculate basic operations\
     and factorial")
    parser.add_argument("-f", "--factorialNum", type=int,
                        help="Input a number to calculate the factorial")
    parser.add_argument("-x", type=float, help="input the number x")
    parser.add_argument("-y", type=float, help="input the number y")
    parser.add_argument(
        "-op",
        "--operation",
        type=str,
        default='',
        help="choose operations: mul(x*y),div(x/y), add(x+y), sub(x-y)"
    )
    args = parser.parse_args()
    # try:
    if len(sys.argv) != 1:
        if args.factorialNum:
            sys.stdout.write(str(factorial(args)))
        elif args.operation:
            sys.stdout.write(str(calculator(args)))
    else:
        print("Execute the script followed by options. Run with -h[--help] to\
 see more options.")


def calculator(args):
    if args.operation == "multiple" or args.operation == "mul":
        return args.x * args.y
    elif args.operation == "divide" or args.operation == "div":
        return args.x / args.y
    elif args.operation == "add" or args.operation == "addition":
        return args.x + args.y
    elif args.operation == "subtract" or args.operation == "sub":
        return args.x - args.y


def factorial(args):
    r = args.factorialNum
    for i in range(1, args.factorialNum):
        r = r * (args.factorialNum - i)
    return r


if __name__ == '__main__':
    main()
