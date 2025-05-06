def validateFirstName(first_name):
    if len(first_name) < 2:
        return f'"{first_name}" is not a valid first name. It is too short.'
    return None

def validateLastName(last_name):
    if len(last_name) < 2:
        return "The last name must be filled in."
    return None

def validateEmployeeID(employee_id):
    if len(employee_id) != 7 or not employee_id[0:2].isalpha() or employee_id[2] != '-' or not employee_id[3:].isdigit():
        return f"{employee_id} is not a valid ID."
    return None

def validateZipCode(zip_code):
    if not zip_code.isdigit():
        return "The ZIP code must be numeric."
    return None

def validateInput(first_name, last_name, zip_code, employee_id):
    errors = []
    
    errors.append(validateFirstName(first_name))
    errors.append(validateLastName(last_name))
    errors.append(validateEmployeeID(employee_id))
    errors.append(validateZipCode(zip_code))
    
    errors = [error for error in errors if error is not None]  # Remove None values
    
    if errors:
        for error in errors:
            print(error)
    else:
        print("There were no errors found.")

# Input prompts
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
zip_code = input("Enter the ZIP code: ")
employee_id = input("Enter an employee ID: ")

validateInput(first_name, last_name, zip_code, employee_id)
