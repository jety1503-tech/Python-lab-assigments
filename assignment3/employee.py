# employees_file.py

FILENAME = "employees.txt"


def add_employee():
    try:
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
    except ValueError:
        print("Salary must be a number.")
        return

    record = f"{emp_id}|{name}|{salary}\n"

    try:
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(record)
        print("Employee added.")
    except OSError:
        print("Error writing to file.")


def display_employees():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No employee file found.")
        return
    except OSError:
        print("Error reading file.")
        return

    if not lines:
        print("No employee records.")
        return

    print("\n--- All Employees ---")
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 3:
            emp_id, name, salary = parts
            print(f"ID: {emp_id}, Name: {name}, Salary: {salary}")


def search_employee_by_name():
    name_to_find = input("Enter name to search: ").strip().lower()

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            found = False
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    emp_id, name, salary = parts
                    if name.lower() == name_to_find:
                        print(f"Record found -> ID: {emp_id}, Name: {name}, Salary: {salary}")
                        found = True
            if not found:
                print("Employee not found.")
    except FileNotFoundError:
        print("No employee file found.")
    except OSError:
        print("Error reading file.")


def main():
    while True:
        print("\n--- Employee Menu ---")
        print("1. Add new employee")
        print("2. Display all employees")
        print("3. Search employee by name")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_employee()
        elif choice == 2:
            display_employees()
        elif choice == 3:
            search_employee_by_name()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
# End of employee.py
