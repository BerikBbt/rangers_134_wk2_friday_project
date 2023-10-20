import random

game =  {}

while True:
    pick = ["rock", "paper", "scissors"]
    computer_choice = random.choice(pick)
    player_choice = input("Pick: (rock, paper, scissors): ")

print(f"\nComputer chose {computer_choice}, player chose {player_choice}. \n")

if computer_choice == player_choice:
    print(f"Both selected {computer_choice}. Game tied")
elif computer_choice == "rock":
    if player_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif computer_choice == "paper":
    if player_choice == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif computer_choice == "scissors":
    if player_choice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")


