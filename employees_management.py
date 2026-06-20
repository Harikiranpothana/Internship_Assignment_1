import json
import os

FILE_NAME = "employees.json"


def load_employees():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
        
            return json.load(file)
    return []


def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


def add_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = {
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Salary": salary
    }

    employees.append(employee)
    save_employees(employees)

    print("\nEmployee added successfully!\n")


def view_employees():
    employees = load_employees()

    if not employees:
        print("\nNo employee records found.\n")
        return

    print("\nEmployee Records")
    print("-" * 60)

    for emp in employees:
        print(f"ID         : {emp['ID']}")
        print(f"Name       : {emp['Name']}")
        print(f"Department : {emp['Department']}")
        print(f"Salary     : {emp['Salary']}")
        print("-" * 60)


def delete_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            save_employees(employees)
            print("\nEmployee deleted successfully!\n")
            return

    print("\nEmployee not found!\n")


def menu():
    while True:
        print("========== Employee Management System ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            delete_employee()

        elif choice == "4":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice! Try again.\n")

def search_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID to search: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            print("\nEmployee Found")
            print("-" * 40)
            print(f"ID         : {emp['ID']}")
            print(f"Name       : {emp['Name']}")
            print(f"Department : {emp['Department']}")
            print(f"Salary     : {emp['Salary']}")
            print("-" * 40)
            return

    print("\nEmployee not found!\n")

    def export_to_csv():
    employees = load_employees()

    if not employees:
        print("\nNo employee records found.\n")
        return

    with open("employees_export.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Department", "Salary"])

        for emp in employees:
            writer.writerow([
                emp["ID"],
                emp["Name"],
                emp["Department"],
                emp["Salary"]
            ])

    print("\nEmployee data exported successfully!")
    print("File created: employees_export.csv\n")
menu()