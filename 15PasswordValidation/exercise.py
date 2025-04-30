correct_password = "abc$123"

user_password = input("What is the password? ")

if user_password == correct_password:
    print("Welcome!")
else:
    print("I don't know you.")
