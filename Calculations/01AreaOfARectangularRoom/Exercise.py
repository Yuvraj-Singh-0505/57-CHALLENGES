SQFT_TO_SQMETERS = 0.09290304

length = float(input("Length of the room in feet? "))
width = float(input("Width of the room in feet? "))

area_sqft = length * width

area_sqmeters = area_sqft * SQFT_TO_SQMETERS

print(f"You entered dimensions of {length} feet by {width} feet.")
print(f"The area is")
print(f"{area_sqft} square feet")
print(f"{area_sqmeters} square meters")
