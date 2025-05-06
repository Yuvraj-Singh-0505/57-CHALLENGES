def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
age = get_valid_input("Enter your age: ")
restingHR = get_valid_input("Enter your resting heart rate: ")

print("\nIntensity | Rate")
print("-------------|--------")

for intensity in range(55, 100, 5):
    targetHR = (((220 - age) - restingHR) * (intensity / 100)) + restingHR
    print(f"{intensity}% | {round(targetHR)} bpm")
