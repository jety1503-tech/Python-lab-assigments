"""
Title: Gradebook Analyzer
Author: [Your Name]
Date: [Insert Date]

Description:
A simple Python program that allows users to enter student marks,
analyze statistics (average, median, max, min), assign grades,
and display a formatted results table with options to re-run the analysis.
"""

import statistics

def calculate_average(marks_dict):
    """Calculate average marks."""
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    """Calculate median marks."""
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    """Find the student with the maximum marks."""
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]

def find_min_score(marks_dict):
    """Find the student with the minimum marks."""
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]

def assign_grades(marks_dict):
    """Assign grades based on marks."""
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def count_grades(grades_dict):
    """Count how many students fall in each grade category."""
    grade_counts = {}
    for grade in grades_dict.values():
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    return grade_counts

def display_results(marks, grades):
    """Display a formatted table of results."""
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name:<12}{marks[name]:<10}{grades[name]}")
    print("-" * 30)

def main_menu():
    """Display the main menu and perform analysis."""
    print("====================================")
    print("     Welcome to Gradebook Analyzer  ")
    print("====================================")

    while True:
        print("\nMenu:")
        print("1. Enter Student Data and Analyze")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '2':
            print("Exiting program. Goodbye!")
            break

        elif choice == '1':
            marks = {}

            # Task 2: Manual data entry
            n = int(input("Enter number of students: "))
            for _ in range(n):
                name = input("Enter student name: ")
                mark = float(input(f"Enter marks for {name}: "))
                marks[name] = mark

            # Task 3: Statistical analysis
            avg = calculate_average(marks)
            med = calculate_median(marks)
            max_name, max_score = find_max_score(marks)
            min_name, min_score = find_min_score(marks)

            print("\n--- Statistical Summary ---")
            print(f"Average Marks: {avg:.2f}")
            print(f"Median Marks: {med:.2f}")
            print(f"Highest Marks: {max_name} ({max_score})")
            print(f"Lowest Marks: {min_name} ({min_score})")

            # Task 4: Grade assignment
            grades = assign_grades(marks)
            grade_counts = count_grades(grades)

            print("\n--- Grade Distribution ---")
            for grade, count in grade_counts.items():
                print(f"Grade {grade}: {count} student(s)")

            # Task 5: Pass/Fail filter
            passed_students = [name for name, m in marks.items() if m >= 40]
            failed_students = [name for name, m in marks.items() if m < 40]

            print("\n--- Pass/Fail Summary ---")
            print(f"Passed Students ({len(passed_students)}): {', '.join(passed_students) if passed_students else 'None'}")
            print(f"Failed Students ({len(failed_students)}): {', '.join(failed_students) if failed_students else 'None'}")

            # Task 6: Results table
            display_results(marks, grades)

        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main_menu()
