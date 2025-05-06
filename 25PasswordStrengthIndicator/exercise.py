def passwordValidator(password):
    has_letter = False
    has_number = False
    has_special = False

    for ch in password:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_number = True
        else:
            has_special = True

    length = len(password)

    if length < 8:
        if has_number and not has_letter and not has_special:
            return 1  # very weak
        elif has_letter and not has_number and not has_special:
            return 2  # weak
    else:
        if has_letter and has_number and not has_special:
            return 3  # strong
        elif has_letter and has_number and has_special:
            return 4  # very strong

    return 0  # unknown/other

password = input("Enter your password: ")
strength = passwordValidator(password)

if strength == 1:
    print("The password '" + password + "' is a very weak password.")
elif strength == 2:
    print("The password '" + password + "' is a weak password.")
elif strength == 3:
    print("The password '" + password + "' is a strong password.")
elif strength == 4:
    print("The password '" + password + "' is a very strong password.")
else:
    print("The password '" + password + "' is of unknown strength.")
