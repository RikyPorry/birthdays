"""Command-line entry point to look up birthdays using the bdpackage module."""

import sys

from bdpackage.bdmodule import return_birthday


def main():
    """Read a person's name from command-line arguments and print their birthday."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <First> <Last>")
        return
    full_name = " ".join(sys.argv[1:])
    return_birthday(full_name)


if __name__ == "__main__":
    main()