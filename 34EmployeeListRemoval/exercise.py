def remove_employee():
    employees = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

    print("There are", len(employees), "employees:")
    for employee in employees:
        print(employee)

    name_to_remove = input("Enter an employee name to remove: ")

    if name_to_remove in employees:
        employees.remove(name_to_remove)
    else:
        print("Employee not found.")

    print("\nThere are", len(employees), "employees:")
    for employee in employees:
        print(employee)

remove_employee()
