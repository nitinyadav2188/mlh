import random

def get_user_choice():
    """Gets the user's choice and validates it."""
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()