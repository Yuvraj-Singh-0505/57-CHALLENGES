import math

p = float(input("What is the principal amount? "))
r = float(input("What is the rate? "))
t = int(input("What is the number of years? "))
n = int(input("What is the number of times the interest is compounded per year? "))

r = r / 100

a = p * (1 + r / n) ** (n * t)
a = math.ceil(a * 100) / 100

print("$" + str(int(p)) + " invested at " + str(r * 100) + "% for " + str(t) + " years")
print("compounded " + str(n) + " times per year is $" + str(format(a, ".2f")) + ".")
