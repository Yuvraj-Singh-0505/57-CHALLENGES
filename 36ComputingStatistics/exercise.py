import math

def compute_statistics():
    times = []

    while True:
        value = input("Enter a number: ")
        if value.lower() == "done":
            break
        try:
            times.append(int(value))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if times:
        total = sum(times)
        average = total / len(times)
        minimum = min(times)
        maximum = max(times)
        variance = sum([(x - average) ** 2 for x in times]) / len(times)
        standard_deviation = math.sqrt(variance)

        print(f"Numbers: {', '.join(map(str, times))}")
        print(f"The average is {average}.")
        print(f"The minimum is {minimum}.")
        print(f"The maximum is {maximum}.")
        print(f"The standard deviation is {standard_deviation:.2f}.")
    else:
        print("No numbers entered.")

compute_statistics()
