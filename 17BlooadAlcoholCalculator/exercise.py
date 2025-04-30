try:
    weight = float(input("Enter your weight in pounds: "))
    gender = input("Enter your gender (male/female): ").lower()
    num_drinks = int(input("Enter the number of drinks consumed: "))
    alcohol_by_volume = float(input("Enter the alcohol by volume (ABV) percentage of the drinks: "))
    hours_since_last_drink = float(input("Enter the number of hours since your last drink: "))

    if gender == "male":
        gender_ratio = 0.73
    elif gender == "female":
        gender_ratio = 0.66
    else:
        raise ValueError("Invalid gender input.")

    total_alcohol = num_drinks * (alcohol_by_volume / 100) * 0.6
    bac = (total_alcohol * 5.14 / weight * gender_ratio) - 0.015 * hours_since_last_drink

    print(f"Your BAC is {bac:.2f}")

    if bac >= 0.08:
        print("It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")
        
except ValueError:
    print("Invalid input. Please enter numeric values where appropriate.")
