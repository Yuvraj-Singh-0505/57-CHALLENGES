#Without using any variablesshadbvhshdbcshvbsjdvbasjdvbasjdvb
print("Hello, " + input("What is your name? ") + ", nice to meet you!")

# Different Greeting for Different People
name = input("What is your name? ")
if name.lower() == "rakesh":
    greeting = "Good Morning Rakesh Sir!"
elif name.lower() == "Shubhi":
    greeting = "Good to see you Shubhi"
elif name.lower() == "yuvraj":
    greeting = "Yuvraj, How are you?"
else:
    greeting = "Hello, " + name + ", nice to meet you!"

print(greeting)
