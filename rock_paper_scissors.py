
# Create a basic rock, paper, scissors program

def rock_paper_scissors(user_choice):

	user_choice = user_choice.lower()

	wins_map = {
		"rock": "scissors",
		"scissors": "paper",
		"paper": "rock"
	}

	import random
	computer_choice = random.randint(0, 2)
	choices = ["rock", "paper", "scissors"]
	computer_choice = choices[computer_choice]

	if user_choice not in wins_map:
		return "Input must be 'rock', 'paper', or 'scissors'. Please try again!"

	print("Computer choice is:", computer_choice)

	if wins_map[computer_choice] == user_choice:
		return "Winner: computer!"

	if wins_map[user_choice] == computer_choice:
		return "Winner: you!"

	if user_choice == computer_choice:
		return "It's a draw!"

user_choice = input("Rock, paper, scissors, shoot! (Type in your choice of weapon) \n" )
print(rock_paper_scissors(user_choice))
