"""Module reading birthdays from CSV and providing lookup helper functions."""

import csv

CSV_FILENAME = "birthdays.csv"


def get_birthdays():
    """Read birthdays.csv and return a dictionary mapping Name -> Birthday."""
    birthdays = {}
    with open(CSV_FILENAME, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name = row["Name"].strip()
            birthday = row["Birthday"].strip()
            birthdays[name] = birthday
    return birthdays


def print_birthdays():
    """Print all names available in the birthdays dictionary."""
    birthdays = get_birthdays()
    print("Welcome to the birthday dictionary. We know the birthdays of these people:")
    for name in birthdays:
        print(name)


def return_birthday(name):
    """Print the birthday of the requested person if present in the CSV data."""
    birthdays = get_birthdays()
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
    else:
        print(f"Sadly, we don't have {name}'s birthday.")