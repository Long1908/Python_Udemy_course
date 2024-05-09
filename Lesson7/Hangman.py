import random

#we are gonna add more flavour to our game and instead of having
#a predefined list of words we are gonna pull a word from the english dictionary.

# 1. Open a file names 'english_words.txt' in READ MODULE 'r'.
#The 'with' statement is used here to ensure that the file is properly closed
#after its suite finished, even if an exception is raised during operation
def generate_random_word():
    with open('words_alpha.txt', 'r') as file:
        words = file.readlines() #Reads all the lines from the file and stores them as a list in the variable 'words'. Each line represents an English word.
    return random.choice(words).strip()
#and last we take a random element from our list 'words' and return it.
#strip() just remove any leading or trailing whitespace characters.

#NOTE!. HOW DOES THE VARIABLE 'words' KNOW HOW TO ACT AS A LIST AND STORE EACH ELEMENT SEPARATELY?
#The behaviour is inherited by the 'readline()' method which takes everything before a newline as a separate element.
#This means that since each word is written in a new line, the variable 'words' stores them as a list of words.
#So to sum up. Each new line is like a new element for a list.

#NOTE!. WHY DO WE NEED TO PROPERLY CLOSE A FILE, EVEN IF WE CAN'T CLOSED
#File closing is important since the memory is allocated for later use.
#If we don't close it, than the recourses used in the memory may not be released, causing data leaks, corruption and data loss.
#Plus if we operate with more files, the memory is finite and we will end up flooding our memory.

random_word = generate_random_word()

display = []
for _ in random_word:
    display.append("_")

print(display)

lives = 6
guessed_the_word = False
guessed_the_character = False
character = []

while not guessed_the_word and lives > 0:
    print(f"You have {lives} lives")
    guess = input("Make your guess: ")
    for i in range(len(random_word)):
        if guess == random_word[i]:
            guessed_the_character = True
            display[i] = guess
    if not character.__contains__(guess):
        character.append(guess)
        if not guessed_the_character:
            print("Oh no!")
            lives -= 1
        else:
            print("Correct!")
    elif character.__contains__(guess):
        print("You have already guessed that letter!")
    guessed_the_word = not display.__contains__("_")
    guessed_the_character = False
    print(display)

if guessed_the_word:
    print("You guessed the word! The word is: " + random_word)

elif lives == 0:
    print("You lost. The word is: " + random_word)

