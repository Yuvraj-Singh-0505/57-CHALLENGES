TAX_RATE = 0.055

price1 = float(input("Price of item 1: "))
qty1 = int(input("Quantity of item 1: "))

price2 = float(input("Price of item 2: "))
qty2 = int(input("Quantity of item 2: "))

price3 = float(input("Enter the price of item 3: "))
qty3 = int(input("Quantity of item 3: "))

subtotal = (price1 * qty1) + (price2 * qty2) + (price3 * qty3)
tax = subtotal * TAX_RATE
total = subtotal + tax

print("Subtotal: ${:.2f}".format(subtotal))
print("Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total))
