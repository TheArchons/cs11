import random

def tieWinLose(player, computer):
    if player == computer:
        print("Tie!")
        return
    if player == "rock":
        if computer == "paper":
            print("You lose! {} beats {}".format(computer, player))
        else:
            print("You win! {} beats {}".format(player, computer))
    if player == "paper":
        if computer == "scissors":
            print("You lose! {} beats {}".format(computer, player))
        else:
            print("You win! {} beats {}".format(player, computer))
    if player == "scissors":
        if computer == "rock":
            print("You lose! {} beats {}".format(computer, player))
        else:
            print("You win! {} beats {}".format(player, computer))

rps = input('rock, paper, or scissors? ')
aiRPS = random.choice(['rock', 'paper', 'scissors'])
if rps == 'rock' or rps == 'paper' or rps == 'scissors':
    tieWinLose(rps, aiRPS)
else:
    print("Invalid input. Pick rock, paper, or scissors.")