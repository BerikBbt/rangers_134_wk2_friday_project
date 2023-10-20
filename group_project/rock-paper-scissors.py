import random

game =  {}

def rock_paper_scissors():   
    while True:
        pick = ["rock", "paper", "scissors"]
        computer_choice = random.choice(pick)
        player_choice = input("Pick: (rock, paper, scissors): ")
        
        print(f"\nComputer chose {computer_choice}, player chose {player_choice}. \n")

        if computer_choice == player_choice.lower():
            print(f"Both selected {computer_choice}. Game Tied.")
        elif computer_choice == "rock":
            if player_choice.lower() == "scissors":
                print("Rock smashes scissors! You lose.")
            else:
                print("Paper covers rock! You win!")
        elif computer_choice == "paper":
            if player_choice.lower() == "rock":
                print("Paper beats rock! You lose.")
            else:
                print("Scissors cuts paper! You win!")
        elif computer_choice == "scissors":
            if player_choice.lower() == "paper":
                print("Scissors beats paper! You lose.")
            else:
                print("Rock smashes scissors! You win!")       
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "n" or play_again.lower() == "no":
            print ("Thank you for playing.")
            break
        else:
            print("Please enter a valid response")
       
rock_paper_scissors()


