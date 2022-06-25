import random

def tieWinLose(player, computer):
    if player == computer: # both inputs are the same
        print("Tie!") # tie
        return
    if player == "rock": # player picked rock
        if computer == "paper": # computer picked paper
            print("You lose! {} beats {}".format(computer, player))
        else: # computer picked scissors
            print("You win! {} beats {}".format(player, computer))
        # the computer couldn't have picked rock because that would've ended in a tie
    if player == "paper": # player picked paper
        if computer == "scissors": # computer picked scissors
            print("You lose! {} beats {}".format(computer, player))
        else: # computer picked rock 
            print("You win! {} beats {}".format(player, computer))
    if player == "scissors": # player picked scissors
        if computer == "rock": # computer picked rock
            print("You lose! {} beats {}".format(computer, player))
        else: # computer picked paper
            print("You win! {} beats {}".format(player, computer))

rps = input('rock, paper, or scissors? ') # user picks rock, paper, or scissors
aiRPS = random.choice(['rock', 'paper', 'scissors']) # ai picks using random.choice
if rps == 'rock' or rps == 'paper' or rps == 'scissors': # if the user input is one the options
    tieWinLose(rps, aiRPS) # determine the winner by calling the function tieWinLose
else: # if input is invalid
    print("Invalid input. Pick rock, paper, or scissors.") # print saying input is invalid