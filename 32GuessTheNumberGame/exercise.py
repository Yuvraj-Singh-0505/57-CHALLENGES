import random

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    print("Let's play Guess the Number.")

    difficulty = get_valid_input("Pick a difficulty level (1, 2, or 3): ")
    
    if difficulty == 1:
        range_end = 10
    elif difficulty == 2:
        range_end = 100
    elif difficulty == 3:
        range_end = 1000
    else:
        print("Invalid difficulty level. Exiting.")
        return

    number_to_guess = random.randint(1, range_end)

    guesses = 0
    while True:
        guess = get_valid_input(f"I have my number. What's your guess? ")
        guesses += 1
        
        if guess < number_to_guess:
            print("Too low. Guess again:")
        elif guess > number_to_guess:
            print("Too high. Guess again:")
        else:
            print(f"You got it in {guesses} guesses!")
            break

    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Goodbye!")

play_game()
