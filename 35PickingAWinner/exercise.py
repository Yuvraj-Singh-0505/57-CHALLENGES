import random

def pick_winner():
    contestants = []

    while True:
        name = input("Enter a name: ")
        if name == "":  
            break
        contestants.append(name)

    if contestants:
        winner = random.choice(contestants)
        print(f"The winner is... {winner}.")
    else:
        print("No contestants were entered.")

pick_winner()
