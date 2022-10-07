player1 = input("Enter a choice for player 1 (rock, paper, scissors): ")
player2 = input("Enter a choice for player 2 (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]


if player1 == player2:
    print(f"Both players selected {player1}. It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Rock smashes scissors! player 1 wins!")
    else:
        print("Paper covers rock! player 2 wins.")
elif player1 == "paper":
    if player2 == "rock":
        print("Paper covers rock!player 1 wins!")
    else:
        print("Scissors cuts paper! player 2 wins")
elif player1 == "scissors":
    if player2 == "paper":
        print("Scissors cuts paper! player 1 wins!")
    else:
        print("Rock smashes scissors! player 2 winss")
