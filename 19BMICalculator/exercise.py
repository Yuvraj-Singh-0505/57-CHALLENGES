weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = (weight / (height * height)) * 703

print("Your BMI is", round(bmi, 1))

if bmi >= 18.5 and bmi <= 25:
    print("You are within the ideal weight range.")
elif bmi < 18.5:
    print("You are underweight. You should see your doctor.")
else:
    print("You are overweight. You should see your doctor.")
