import random
import string

def generate_password():
    min_length = int(input("What's the minimum length? "))
    num_special = int(input("How many special characters? "))
    num_numbers = int(input("How many numbers? "))

    special_characters = ['$', '#', '@', '!', '%', '&', '*', '(', ')']
    numbers = string.digits
    letters = string.ascii_lowercase + string.ascii_uppercase

    password = []

    for _ in range(num_special):
        password.append(random.choice(special_characters))

    for _ in range(num_numbers):
        password.append(random.choice(numbers))

    while len(password) < min_length:
        password.append(random.choice(letters))

    random.shuffle(password)
    generated_password = ''.join(password)
    
    print(f"Your password is\n{generated_password}")

generate_password()
