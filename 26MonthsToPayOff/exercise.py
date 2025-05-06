import math

def calculateMonthsUntilPaidOff(balance, apr, monthly_payment):
    i = (apr / 100) / 365  # daily rate
    n = (-1 / 30) * math.log(1 + (balance / monthly_payment) * (1 - (1 + i) ** 30)) / math.log(1 + i)
    return math.ceil(n)  # Round up to the nearest whole number

balance = float(input("What is your balance? "))
apr = float(input("What is the APR on the card (as a percent)? "))
monthly_payment = float(input("What is the monthly payment you can make? "))

months = calculateMonthsUntilPaidOff(balance, apr, monthly_payment)

print(f"It will take you {months} months to pay off this card.")
