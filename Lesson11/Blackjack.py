import random
import time

# Code can use some cleaning and there are other functionality that should be checked and made correctly.
# Everything works, it's for splitting pairs does not work fully correctly for the true Blackjack rule.

deck = {
    "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
    "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
    "hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
    "diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
}

card_value = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [1, 11]
}


def stand(hand):
    return hand


def random_card_generator():
    suits = list(deck)
    random_suit = random.choice(suits)
    random_card = random.choice(deck[random_suit])
    deck[random_suit].remove(random_card)
    return random_card


def deal_hand():
    hand = []
    for cards in range(0, 2):
        random_card = random_card_generator()
        hand.append(random_card)
    return hand


def draw_card(hand):
    random_card = random_card_generator()
    hand.append(random_card)
    return hand


def hit(hand):
    dummy_hand = hand
    draw_card(dummy_hand)
    print(f"This is your hand: {dummy_hand}.")
    again = input("Would you like to hit again? (y/n)").lower().strip()
    while not (again == "y" or again == "n"):
        print("I am sorry but the answer you have given is invalid. Please write y or n")
        again = input("Would you like to hit again? (y/n)").lower().strip()
    if again == "y":
        hit(dummy_hand)
    else:
        hand = dummy_hand
    return hand


def calculate_points_in_hand(hand, ace_index):
    """By default the calculation will calculate at first with an ace index of 0, which basically means the ace will have a value of 11.
    If the total point exceeds 21, then the program will calculate the total points, where the ace index is 1, which means the
    Ace will have a value of 1.
    So we must always call this function with second argument 0"""
    total_points = 0
    for card in hand:
        if card == "A":
            total_points += card_value[card][ace_index]
        else:
            total_points += card_value[card]
    if total_points > 21 and ace_index == 1:
        calculate_points_in_hand(hand, 0)
    else:
        return total_points
#use sum() and check if ace calculates correctly.


def check_for_blackjack(hand):
    if len(hand) == 2:
        if calculate_points_in_hand(hand, 1) == 21:
            return True
        else:
            return False
    else:
        return False


def splitting_pairs(hand):
    my_first_hand = []
    my_first_hand.append(hand[0])
    my_second_hand = []
    my_second_hand.append(hand[1])
    draw_card(my_first_hand)
    draw_card(my_second_hand)
    print(f"Your hands are now {my_first_hand} and {my_second_hand}.")
    draw = input("Would you like to draw cards? (y/n): ").lower().strip()
    while draw not in ['y', 'n']:
        print("I am sorry but the answer you have given is invalid. Please write y or n")
        draw = input("Would you like to draw cards? (y/n): ").lower().strip()
    while draw == 'y':
        draw_card(my_first_hand)
        draw_card(my_second_hand)
        print(f"Your hands are now {my_first_hand} and {my_second_hand}.")
        if my_first_hand[0] == "A" and my_second_hand[0] == "A":
            print("You cannot draw any more cards, since you split double Aces.")
            draw = 'n'
        else:
            draw = input("Would you like to draw cards? (y/n): ").lower().strip()
            while draw not in ['y', 'n']:
                print("I am sorry but the answer you have given is invalid. Please write y or n")
                draw = input("Would you like to draw cards? (y/n): ").lower().strip()
    my_first_hand_points = calculate_points_in_hand(my_first_hand, 1)
    my_second_hand_points = calculate_points_in_hand(my_second_hand, 1)
    if my_first_hand_points >= my_second_hand_points:
        if my_first_hand_points > 21:
            if my_second_hand_points > 21:
                return my_first_hand
            else:
                return my_second_hand
        else:
            return my_first_hand
    else:
        if my_second_hand_points > 21:
            if my_first_hand_points > 21:
                return my_second_hand
            else:
                return my_first_hand
        else:
            return my_second_hand


def doubling_down(hand):
    draw_card(hand)
    return hand


def surrender(hand):
    stand(hand)


legit_moves = {
    "hit": hit,
    "stand": stand,
    "splitting pairs": splitting_pairs,
    "doubling down": doubling_down,
    "surrender": surrender,
}


def play(money):
    print("Minimum bet is 5$.")
    if money < 5:
        print("You cannot continue with this amount of money on this table. You will have to stand up")
        return money
    pot = 5
    pot_for_insurance = 0
    insurance_enabled = False
    add_to_pot = input("Would you like to bet more? (y/n): ").lower().strip()
    while not add_to_pot == "y" and not add_to_pot == "n":
        print("I am sorry but the answer you have given is invalid. Please write y or n")
        add_to_pot = input("Would you like to bet more? (y/n): ").lower().strip()
    if add_to_pot == 'y':
        if money == pot:
            print("I am sorry, but it seems you don't have any more money to add on. We will continue with your minimum bet.")
        else:
            bet = input("How much would you like to bet: ").strip()
            while not bet.isnumeric():
                print("I am sorry but your input is not valid. We need you to enter how much money are you betting.")
                bet = input("How much would you like to bet: ").strip()
            bet = int(bet)
            pot += bet
    my_hand = deal_hand()
    print(f"This is your hand: {my_hand}.")
    computer_hand = deal_hand()
    if check_for_blackjack(my_hand):
        print("You have a Blackjack!")
        if not check_for_blackjack(computer_hand):
            print(f"You win! You get {pot}$")
            money += pot
        else:
            print(f"Dealer also has blackjack! It's a push. No winner.")
        print(f"This is how much money you have now {money}")
        play_again = input("Would like to play again? (y/n):").lower().strip()
        while not play_again == 'y' and not play_again == 'n':
            print("I am sorry but the answer you have given is invalid. Please write y or n")
            play_again = input("Would like to play again? (y/n):").lower().strip()
        if play_again == 'y':
            play(money)
        else:
            return money
    print(f"This is the dealer's hand: [{computer_hand[0]}, *].")
    if computer_hand[0] == "A":
        print("The dealer shows an Ace. This means that you have a chance to play 'Insurance'.\nWhat 'Insurance' is, it gives you a chance to bet a second pot solely for the chance that the dealer has a Blackjack.")
        insurance_choice = input("Would you like to do it? (y/n):").lower().strip()
        while not (insurance_choice == 'y'or insurance_choice == 'n'):
            print("Please enter a correct answer.")
            insurance_choice = input("Would you like to do it? (y/n):").lower().strip()
        if insurance_choice == 'y':
            insurance_enabled = True
            pot2 = input("How much would you like to bet that the dealer has ").strip()
            while not pot2.isnumeric():
                print("Please enter a numeric value for the bet.")
                pot2 = input("How much would you like to bet that the dealer has ").strip()
            pot_for_insurance = int(pot2)
    current_moves = list(legit_moves)
    action = input(f"What would you like to do {current_moves}:").lower().strip()
    while action not in current_moves:
        print(f"What you entered is not a valid command. Please choose a valid command. ")
        action = input(f"What would you like to do {current_moves}: ").lower().strip()
    function = legit_moves[action]
    if function == splitting_pairs:
        print(f"Your hand now is gonna split, which means you need to match your bet for the second hand,\nmaking your bet now: {pot * 2}")
        pot *= 2
    if function == doubling_down:
        print(f"You you are Doubling down, which means you are doubling the bet and can only hit one card. Your bet now is: {pot * 2}")
        pot *= 2
    my_hand = function(my_hand)
    print(f"This is your hand: {my_hand}.")
    my_hand_points = calculate_points_in_hand(my_hand, 1)
    print(f"Your hand has {my_hand_points} points.")
    if my_hand_points > 21 or my_hand_points == 0:
        print(f"Your hand is busted. You lose {pot}$!")
        money -= pot
    else:
        print(f"This is the computer's hand: {computer_hand}")
        if check_for_blackjack(computer_hand):
            print(f"The dealer has a Blackjack! That means that you lose the original bet of {pot}$ amount.")
            if insurance_enabled:
                print(f"You however made the insurance play, which means you win back: {pot_for_insurance}")
        elif insurance_enabled:
            print(f"Dealer has no Blackjack. You lose {pot_for_insurance}")
        else:
            time.sleep(2)
            computer_hand_points = calculate_points_in_hand(computer_hand, 1)
            while computer_hand_points < 17 or computer_hand_points < my_hand_points:
                print("Computer will hit.")
                draw_card(computer_hand)
                print(f"This is the computer's hand: {computer_hand}")
                time.sleep(2)
                computer_hand_points = calculate_points_in_hand(computer_hand, 1)

            if computer_hand_points > 21:
                print(f"The dealer is busted. You win {pot}$!")
                money += pot
            elif computer_hand_points == my_hand_points:
                print(f"The computer has {computer_hand_points} points.")
                print(f"It's a tie. No money is won or lost.")
            else:
                print(f"The computer has {computer_hand_points} points.")
                print(f"You lose {pot}$.")
                money -= pot
    print(f"This is how much money you have now {money}")
    if money < 5:
        print("Sorry, but you can't play on this table no more. Have a nice day/evening.")
    play_again = input("Would like to play again? (y/n):").lower().strip()
    while not play_again == 'y' and not play_again == 'n':
        print("I am sorry but the answer you have given is invalid. Please write y or n")
        play_again = input("Would like to play again? (y/n):").lower().strip()
    if play_again == 'y':
        play(money)


print("Welcome to our Black Jack Python table!")
entry_money = input("How much money are you entering with on this table?")
while not entry_money.isnumeric() or not int(entry_money) >= 5:
    print("I am sorry but your input is not valid.\nWe need you to enter how much money are you entering with and your entry needs to be minimum of 5$.")
    entry_money = input("How much money are you entering with on this table?")
entry_money = int(entry_money)
print("Splendid! Let us begin our game!")
play(entry_money)


