"""Script to export the initial birthdays dictionary into a CSV file."""

import csv

BIRTHDAYS = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
    "Donald Trump": "06/14/1946",
    "Rowan Atkinson": "01/6/1955",
}


def main():
    """Write the birthdays dictionary to birthdays.csv with Name and Birthday columns."""
    with open("birthdays.csv", mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Birthday"])
        for name, birthday in BIRTHDAYS.items():
            writer.writerow([name, birthday])


if __name__ == "__main__":
    main()