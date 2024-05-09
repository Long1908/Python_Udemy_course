import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
all_moves = ["Rock", "Paper", "Scissors"]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors!"))
if my_choice == 0:
    print("I choose\n" + rock)
elif my_choice == 1:
    print("I choose\n" + paper)
else:
    print("I choose\n" + scissors)

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer choose\n" + rock)
elif computer_choice == 1:
    print("Computer choose\n" + paper)
else:
    print("Computer choose\n" + scissors)

if computer_choice == my_choice:
    print("It's a tie!")
else:
    if all_moves[my_choice - 1] == all_moves[computer_choice]:
        print("I win!")
    else:
        print("I lose!")


