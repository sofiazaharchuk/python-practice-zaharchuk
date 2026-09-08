def read_grade(prompt):
    """Ask for a grade until a valid integer from 0 to 100 is entered."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Error: digits only")
            continue
        grade = int(value)
        if 0 <= grade <= 100:
            return grade
        print("Error: the value must be between 0 and 100")


def to_letter(grade):
    """Convert a numeric grade into a letter grade."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Return the arithmetic mean of a list of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Return how many grades are greater than limit."""
    count = 0
    for grade in grades:
        if grade > limit:
            count += 1
    return count


def print_report(name, group, grades):
    """Print a short report for one student."""
    avg = average(grades)
    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", " ".join(str(g) for g in grades))
    print(f"Average: {avg:.2f} -> {to_letter(round(avg))}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main():
    """Entry point of the program."""
    name = "Sofia Zaharchuk"
    group = "IT-32"
    print(f"{name}, {group}")

    n = len("Sofia")
    grades = []
    for i in range(1, n + 1):
        grades.append(read_grade(f"Grade {i} (0-100): "))

    print_report(name, group, grades)


main()
