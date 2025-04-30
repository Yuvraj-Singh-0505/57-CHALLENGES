choice = input("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\nYour choice: ").lower()

if choice == 'c':
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"The temperature in Celsius is {celsius:.1f}.")
elif choice == 'f':
    celsius = float(input("Please enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit:.1f}.")
else:
    print("Invalid choice.")
