"""Command-line interface using argparse and dynamic choices from birthdays.csv."""

import argparse

from bdpackage.bdmodule import get_birthdays, return_birthday


def get_name_choices():
    """Extract sorted unique first names and last names from get_birthdays()."""
    birthdays = get_birthdays()
    firstnames = set()
    lastnames = set()

    for full_name in birthdays:
        parts = full_name.strip().split()
        if len(parts) >= 2:
            firstnames.add(parts[0])
            lastnames.add(" ".join(parts[1:]))
        elif len(parts) == 1:
            firstnames.add(parts[0])

    return sorted(firstnames), sorted(lastnames)


def parse_args(firstname_choices, lastname_choices):
    """Parse and return command-line arguments using dynamic choices."""
    parser = argparse.ArgumentParser(
        description="Look up a person's birthday by first name and last name."
    )
    parser.add_argument(
        "--firstname",
        required=True,
        choices=firstname_choices,
        help="Provide your first name (e.g., --firstname Albert)",
    )
    parser.add_argument(
        "--lastname",
        required=True,
        choices=lastname_choices,
        help="Provide your last name (e.g., --lastname Einstein)",
    )
    return parser.parse_args()


def main():
    """Run the birthday lookup using dynamically loaded choices."""
    firstname_choices, lastname_choices = get_name_choices()
    args = parse_args(firstname_choices, lastname_choices)
    full_name = f"{args.firstname} {args.lastname}"
    return_birthday(full_name)


if __name__ == "__main__":
    main()