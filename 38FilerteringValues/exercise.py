def filterEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
    input_str = input("Enter a list of numbers, separated by spaces: ")
    number_list = [int(x) for x in input_str.split()]

    even_numbers = filterEvenNumbers(number_list)

    print(f"The even numbers are {' '.join(map(str, even_numbers))}.")
    
main()
