import random
def rock_paper_scissors():
    choices = ["rock","paper","scissors"]
    player_score = 0
    computer_score = 0


    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to end): ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}\n")
    
    
    print("\n--- Game Over ---")
    print(f"Final score - You: {player_score}, Computer: {computer_score}")
if __name__ == "__main__":
    rock_paper_scissors() 