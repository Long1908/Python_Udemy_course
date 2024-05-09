import random
#task 1
word_list = ["ardvark", "baboon", "camel"]

#Todo1 -Randomly choose a word from a word_list and assign it to a variable called chosen _word
chosen_word = random.choice(word_list)

#Todo2 - Ask the user to guess a ltter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter: ").lower()

#todo3 - Check if the letter the user guessed(guess) is one of the letters in the chosen_word
guess_correctness = False
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        guess_correctness = True
print(f"Your word is {chosen_word} and you guess is {guess_correctness}.")

#Or we can write :
for i in chosen_word:
    if guess == i:
        guess_correctness = True
print(f"Your word is {chosen_word} and you guess is {guess_correctness}.")

guess_chart = []
#task 2
#Todo1 - Create and empty list called display. For each letter in the choosen_Word,
#add a "_" 'display.
#So if the chossen_word was "apple", display should be ["_","_","_","_","_"].

#Todo2 - Loop through each position in the chosen_Word;
#if the ltter at the position matches 'guess then reveal that letter
#the display at that position.

#Todo3 - Print 'display' and you should see the guessed letter
for i in chosen_word:
    guess_chart.append('_')

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        guess_chart[i] = guess
print(guess_chart)

#task3
#Basically we are gonna complete the game by making it possible for the
#player to keep looping and guessing until he or she guess the word
#or the lives are finished.
#So we can check the final product of 'Hangman' and there is the whole functionality.

