import math

order_amount = float(input("What is the order amount? "))
state = input("What state do you live in? ")

tax = 0

if state == "Wisconsin":
    county = input("What county do you live in? ")
    tax_rate = 0.05
    if county == "Eau Claire":
        tax_rate = tax_rate + 0.005
    elif county == "Dunn":
        tax_rate = tax_rate + 0.004
    tax = math.ceil(order_amount * tax_rate * 100) / 100
elif state == "Illinois":
    tax_rate = 0.08
    tax = math.ceil(order_amount * tax_rate * 100) / 100

total = math.ceil((order_amount + tax) * 100) / 100

if tax > 0:
    print("The tax is $" + str(tax))
    print("The total is $" + str(total))
else:
    print("The total is $" + str(total))
