import cs50
from sys import argv, exit


def main():
    # Usage: python roster.py house
    # python roster.py Gryffindor

    if len(argv) != 2:
        exit("Usage: python roster.py house")

    house = argv[1]

    # Open the database
    db = cs50.SQL("sqlite:///students.db")

    students = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house)

    for student in students:
        if student["middle"] == None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")


if __name__ == "__main__":
    main()
