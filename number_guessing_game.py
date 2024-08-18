from art import logo
import random
print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(computer, user, turns):
    if user > computer:
        print("Too high")
        return turns - 1
    elif user < computer:
        print("Too low")
        return turns - 1
    else:
        print(f"You are right👍 the answer was {computer}")
        return 

def game():

    answer = random.randint(1, 100)
    guess = 0
    turns = set_difficulty()

    # print(f"Psst answer is {answer}")

    while guess != answer:
        print(f"You have {turns} attempts remaining")

        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)

        if turns == 0:
            print("You've run out of guesses, you loss!")
            return
        elif guess != answer:
            print("Guess again")
game()