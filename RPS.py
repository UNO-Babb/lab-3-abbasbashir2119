# RPS.py
# Name: [Your Name]
# Date: [Today's Date]
# Assignment: Rock–Paper–Scissors Game

import random

def main():
    wins = 0
    ties = 0
    losses = 0

    # Define the valid moves.
    moves = ['R', 'P', 'S']

    print("Welcome to Rock-Paper-Scissors!")
    
    # Create a loop that continues as long as the user wishes to play.
    play_again = True
    while play_again:
        # Randomly choose the computer's move.
        computer_move = random.choice(moves)
        
        # Prompt the user for their RPS selection.
        user_move = input("Enter your move (R, P, or S): ").upper()
        while user_move not in moves:
            user_move = input("Invalid input. Please enter R, P, or S: ").upper()

        print("Computer chose:", computer_move)

        # Determine the winner.
        if user_move == computer_move:
            print("It's a tie!")
            ties += 1
        elif ((user_move == 'R' and computer_move == 'S') or
              (user_move == 'S' and computer_move == 'P') or
              (user_move == 'P' and computer_move == 'R')):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

        # Ask the user if they would like to play again.
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer != 'y':
            play_again = False
        print()  # Blank line for better readability between rounds

    # Print the final stats.
    print("\nFinal Stats:")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(f"{wins}\t{ties}\t{losses}")

if __name__ == '__main__':
    main()
