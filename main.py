#!/usr/bin/env python3
import parser
from dispatch import dispatch


def main():
    args = parser.run()
    dispatch(args)
    print("Hello, world!")


if __name__ == "__main__":
    main()
