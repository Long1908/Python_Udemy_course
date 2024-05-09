import random

level = {
    "easy": 10,
    "hard": 5,
}

number_we_need_to_guess = random.randint(0, 101)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")
difficulty = input("What difficulty would you like to guess? ").strip().lower()
if difficulty not in list(level):
    print("Sorry, that's not a valid difficulty choice.")
    difficulty = input("What difficulty would you like to guess? ").strip().lower()
trials = level[difficulty]
while trials != 0:
    print(f"You have {trials} guesses left.")
    guess = input("Make a guess: ").strip()
    if not guess.isnumeric():
        print("Sorry, that's not a valid number.")
        guess = input("Make a guess: ").strip()
    guess = int(guess)
    if not guess == number_we_need_to_guess:
        if trials == 1:
            print(f"You failed to guess.\nThe number is {number_we_need_to_guess}")
        else:
            if guess < number_we_need_to_guess:
                print("Too low.")
            else:
                print("Too high.")
            print("Guess again.")
            trials -= 1
    else:
        print("Congratulation. You guessed the correct number.")
        trials = 0

