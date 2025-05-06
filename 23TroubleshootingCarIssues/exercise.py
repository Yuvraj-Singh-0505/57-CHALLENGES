answer = input("Is the car silent when you turn the key? (y/n): ")

if answer == "y":
    answer = input("Are the battery terminals corroded? (y/n): ")
    if answer == "y":
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")
else:
    answer = input("Does the car make a clicking noise? (y/n): ")
    if answer == "y":
        print("Replace the battery.")
    else:
        answer = input("Does the car crank up but fail to start? (y/n): ")
        if answer == "y":
            print("Check spark plug connections.")
        else:
            answer = input("Does the engine start and then die? (y/n): ")
            if answer == "y":
                answer = input("Does your car have fuel injection? (y/n): ")
                if answer == "y":
                    print("Get it in for service.")
                else:
                    print("Check to ensure the choke is opening and closing.")
            else:
                print("This should not be possible.")
