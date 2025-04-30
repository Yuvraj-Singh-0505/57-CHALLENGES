import math
PER_GALLON = 350
length = float(input("Length : "))
width = float(input("Width : "))
area = length * width
gallons_needed = math.ceil(area / PER_GALLON)
print(f"{gallons_needed} gallons of paint to cover {int(area)} square feet.")
