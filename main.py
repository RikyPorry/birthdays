"""Command-line interface using argparse to look up birthdays."""

import argparse

from bdpackage.bdmodule import return_birthday

FIRSTNAME_CHOICES = ["Albert", "Benjamin", "Ada", "Donald", "Rowan"]
LASTNAME_CHOICES = ["Einstein", "Franklin", "Lovelace", "Trump", "Atkinson"]


def parse_args():
    """Parse and return command-line arguments for firstname and lastname."""
    parser = argparse.ArgumentParser(
        description="Look up a person's birthday by first name and last name."
    )
    parser.add_argument(
        "--firstname",
        required=True,
        choices=FIRSTNAME_CHOICES,
        help="Provide your first name (e.g., --firstname Albert)",
    )
    parser.add_argument(
        "--lastname",
        required=True,
        choices=LASTNAME_CHOICES,
        help="Provide your last name (e.g., --lastname Einstein)",
    )
    return parser.parse_args()


def main():
    """Run the birthday lookup using parsed CLI arguments."""
    args = parse_args()
    full_name = f"{args.firstname} {args.lastname}"
    return_birthday(full_name)


if __name__ == "__main__":
    main()