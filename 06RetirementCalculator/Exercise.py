import datetime

current_year = datetime.datetime.now().year

current_age = int(input("What is your current age? "))
retirement_age = int(input("At what age would you like to retire? "))

years_left = retirement_age - current_age

retirement_year = current_year + years_left

print(f"You have {years_left} years left until you can retire.")
print(f"It's {current_year}, so you can retire in {retirement_year}.")
