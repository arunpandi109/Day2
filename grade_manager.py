# Student Grade Manager
# grade_manager.py


def calculate_grade(mark):
    """Return the grade for a given mark."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student(students):
    """Ask for student details and add them to the list."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    while True:
        mark_input = input("Enter mark (0-100): ").strip()

        try:
            mark = float(mark_input)

            if mark < 0 or mark > 100:
                print("Error: Mark must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")


    grade = calculate_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"Student '{name}' added successfully.")


def show_students(students):
    """Display all students and class statistics."""
    if not students:
        print("\nNo students have been added yet.")
        return

    print("\n" + "=" * 45)
    print("STUDENT RESULTS")
    print("=" * 45)

    print(f"{'Name':<20}{'Mark':>10}{'Grade':>10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:>10.2f}"
            f"{student['grade']:>10}"
        )

    print("-" * 40)

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Class average: {average:.2f}")
    print(f"Highest mark:  {highest:.2f}")
    print(f"Lowest mark:   {lowest:.2f}")
    print("=" * 45)


def main():
    """Run the Student Grade Manager."""
    students = []

    while True:
        print("\nSTUDENT GRADE MANAGER")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Error: Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
