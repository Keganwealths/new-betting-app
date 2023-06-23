import random

while True:
    # Get the three odds from the user
    home_odd = float(input("Enter the home odd: "))
    draw_odd = float(input("Enter the draw odd: "))
    away_odd = float(input("Enter the away odd: "))

    # Ask the user which odd they think will win
    user_pick = input("Which odd do you think will win (home/draw/away)? ").lower()

    # Calculate the winning percentage of the remaining odds
    if user_pick == "home":
        winning_percentage = draw_odd / (draw_odd + away_odd) * 100
        least_percentage_odd = min(draw_odd, away_odd)
    elif user_pick == "draw":
        winning_percentage = home_odd / (home_odd + away_odd) * 100
        least_percentage_odd = min(home_odd, away_odd)
    elif user_pick == "away":
        winning_percentage = home_odd / (home_odd + draw_odd) * 100
        least_percentage_odd = min(home_odd, draw_odd)

    # Pick a random odd between the user's pick and the least percentage odd
    random_odd = random.choice([user_pick, least_percentage_odd])

    # Print the prediction to the user
    if random_odd == user_pick:
        print(f"You win! The {user_pick} odd wins.")
    else:
        print(f"The game will end in a {random_odd}.")

    # Ask the user if they want to enter more odds
    choice = input("Do you want to enter more odds? (y/n) ")
    if choice.lower() == "n":
        break
