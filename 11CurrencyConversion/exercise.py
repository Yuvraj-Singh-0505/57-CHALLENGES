import math

euros = float(input("How many euros are you exchanging? "))
rate = float(input("What is the exchange rate? "))

usd = math.ceil((euros * rate) * 100) / 100  

print(f"{euros:.0f} euros at an exchange rate of {rate:.2f} is {usd:.2f} U.S. dollars.")
