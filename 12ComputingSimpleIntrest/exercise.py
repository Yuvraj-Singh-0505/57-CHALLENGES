import math

p = float(input("Enter the principal: "))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the number of years: "))

r = r / 100

a = p * (1 + r * t)

a = math.ceil(a * 100) / 100

print("After", t, "years at", r * 100, "%, the investment will be worth $", format(a, ".2f"), ".", sep="")
