action = input("What would you like to do (Splitting Pairs/Doubling Down/Insurance/Surrender):").lower()
while action not in ["splitting pairs", "doubling down", "insurance", "surrender"]:
    print("I am sorry but that is not a valid move. Please choose a valid option")
    action = input("What would you like to do (Splitting Pairs/Doubling Down/Insurance/Surrender):").lower()