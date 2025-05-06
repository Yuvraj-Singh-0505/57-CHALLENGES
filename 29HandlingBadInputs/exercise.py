def get_rate_of_return():
    while True:
        rate = input("What is the rate of return? ")
        if rate.isdigit():
            rate = float(rate)
            if rate == 0:
                print("Sorry. That's not a valid input.")
            else:
                return rate
        else:
            print("Sorry. That's not a valid input.")
rate_of_return = get_rate_of_return()
years = 72 / rate_of_return
print(f"It will take {years} years to double your initial investment.")
