import random

options = ["rock", "paper", "scissors"]
name = input("Enter your name : ")
computer_Score = 0 
player_Score = 0
running = True
print(f"Welcome {name.title()}")

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in options:
            print("That's not a valid option. Check your spelling!")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print(f"{name.title()} wins. Computer loses.")
        player_Score += 1
    elif player == "paper" and computer == "rock":
        print(f"{name.title()} wins. Computer loses.")
        player_Score += 1
    elif player == "scissors" and computer == "paper":
        print(f"{name.title()} wins. Computer loses.")
        player_Score += 1
    else:
        print(f"{name.title()} loses. Computer wins.")
        computer_Score += 1

    print(f"{name.title()}: {player_Score} | Computer: {computer_Score}")

    play_again = None
    while play_again not in ("yes", "no"):
        play_again = input("Play again? (yes/no): ").lower()
        if play_again not in ("yes", "no"):
            print("Not a valid response. Type 'yes' to play again or 'no' to quit.")

    if play_again == "no":
        running = False

print(f"{name.title()}: {player_Score} | Computer: {computer_Score}")

if player_Score == computer_Score:
    print("It's a tie!")
elif player_Score > computer_Score:
    print(f"Congrats {name.title()}, You won the game!!")
else:
    print(f"Oops Computer won the game!! Better luck next time!")

print("Thanks for playing!!")
