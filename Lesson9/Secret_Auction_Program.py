players_and_bid={}
print("Welcome to Secret Auction Program")
name = input("What is your name?: ")
bid = int(input("What is your bid?: $ "))
players_and_bid[name] = bid
more_players = input("Are there any other bidders?(y/n): ")
while not more_players == "y" and not more_players == "n":
    print("Sorry, that's not a valid option. Please try again.")
    more_players = input("Are there any other bidders?(y/n): ")

while more_players == "y":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    players_and_bid[name] = bid
    more_players = input("Are there any other bidders?(y/n): ")
    while not more_players == "y" and not more_players == "n":
        print("Sorry, that's not a valid option. Please try again.")
        more_players = input("Are there any other bidders?(y/n): ")

max_bid = 0
player_with_max_bid = ""
for player in players_and_bid:
    if players_and_bid[player] > max_bid:
        player_with_max_bid = player
        max_bid = players_and_bid[player]

print(f"Congratulations! {player_with_max_bid} has won, with a bid of {max_bid}!")