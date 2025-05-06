import random

def magic_8_ball():
    responses = ["Yes", "No", "Maybe", "Ask again later"]

    question = input("What's your question? ")

    answer = random.choice(responses)

    print(answer)

magic_8_ball()
