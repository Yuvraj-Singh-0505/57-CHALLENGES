# Prompting the user for two numbers
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

# Converting input strings to numbers
num1 = float(num1)
num2 = float(num2)

# Printing the results with a single output statement
print(f"{num1} + {num2} = {num1 + num2}\n{num1} - {num2} = {num1 - num2}\n{num1} * {num2} = {num1 * num2}\n{num1} / {num2} = {num1 / num2}")
