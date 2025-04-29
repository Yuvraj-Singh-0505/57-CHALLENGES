people = int(input("How many people are there? "))
pizzas = int(input("How many pizzas do you have? "))
slices_per_pizza = int(input("How many slices per pizza? "))

total_slices = pizzas * slices_per_pizza

slices_per_person = total_slices // people
leftover_slices = total_slices % people

print(f"{people} people with {pizzas} pizzas")
print(f"Each person gets {slices_per_person} pieces of pizza.")
print(f"There are {leftover_slices} leftover pieces.")
