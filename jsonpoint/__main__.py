import argparse
from sys import stdin


def main():

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('pointer', help='')
    parser.add_argument('--input', default=stdin, help='', required=False)

    args = parser.parse_args()

    from jsonpoint import get

    print get(args.input.read(), args.pointer)


if __name__ == "__main__":
    main()
