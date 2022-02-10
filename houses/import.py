from cs50 import SQL
import csv
from sys import argv, exit


def main():
    # Usage: python import.py filename.csv
    # python import.py characters.csv

    if len(argv) != 2:
        exit("Usage: python import.py filename.csv")

    # Open CSV file
    with open(argv[1], "r") as file:

        # Create DictReader
        reader = csv.DictReader(file)

        # May assume columns will be name, house, and birth

        # Open the database
        db = SQL("sqlite:///students.db")

        # Iterate over CSV file
        for row in reader:
            name = row['name'].split()
            if len(name) == 3:
                first = name[0]
                middle = name[1]
                last = name[2]
            else:
                first = name[0]
                middle = None
                last = name[1]

            # Insert student into database
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first, middle, last, row["house"], row["birth"])


if __name__ == "__main__":
    main()
