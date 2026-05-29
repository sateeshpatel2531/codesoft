import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
print("   ROCK PAPER SCISSORS GAME")
print("Instructions:")
print("Type rock, paper, or scissors")
print("Enter 'exit' anytime to quit the game")
while True:
    user_choice = input("Enter your choice: ").lower()
    if user_choice == "exit":
        print("Thanks for playing")
        break
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")
    if user_choice == computer_choice:
        print("Result: It's a Tie")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win")
        user_score += 1
    else:
        print("Result: Computer Wins")
        computer_score += 1
    print("SCORE BOARD")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Final Scores")
        print(f"Your Score     : {user_score}")
        print(f"Computer Score : {computer_score}")
        print("Game Over Thanks for playing.")
        break