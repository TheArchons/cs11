import random, os, json

def determineWinner(playerChoice):
    computerChoice = random.choice(['rock', 'paper', 'scissors']) # pick a random choice from the list

    if playerChoice == computerChoice:
        print('Tie! You both chose ' + playerChoice)
        return 'tie'
    elif playerChoice == 'rock':
        if computerChoice == 'paper':
            print('Computer wins! Paper beats rock.')
            return 'computer'
        else:
            print('Player wins! Rock beats scissors.')
            return 'player'
    elif playerChoice == 'paper':
        if computerChoice == 'scissors':
            print('Computer wins! Scissors beats paper.')
            return 'computer'
        else:
            print('Player wins! Paper beats rock.')
            return 'player'
    elif playerChoice == 'scissors':
        if computerChoice == 'rock':
            print('Computer wins! Rock beats scissors.')
            return 'computer'
        else:
            print('Player wins! Scissors beats paper.')
            return 'player'

# note: I used json over a txt file because it is easier to read and write

if os.path.exists('rpsScores.json'): # load scores from the json file if it exists
    with open('rpsScores.json', 'r') as f:
        scores = json.load(f)
        playerScore = scores['player']
        computerScore = scores['computer']
else: # else, set the scores to 0
    playerScore = 0
    computerScore = 0

while True:
    userChoice = input("rock, paper, or scissors? (type 'exit' to quit the program, reset to reset your scores) ") # takes an input from the user

    if userChoice == "exit": # if exit was entered, break the loop, quitting the program
        break
    
    if userChoice == 'reset': # if reset was entered, reset the scores to 0 and continue the loop
        playerScore = 0
        computerScore = 0
        with open('rpsScores.json', 'w') as f:
            json.dump({'player': playerScore, 'computer': computerScore}, f)
        print('Scores reset to 0.', end='\n\n') # tell the user scores have been reset
        continue

    if userChoice not in ['rock', 'paper', 'scissors']: # if the user entered an invalid choice (not equal to rock, paper, or scissors), print an error message and continue the loop
        print("Invalid choice. Please try again.", end="\n\n") # 2 newlines to separate the error message from the next prompt
        continue
    
    winner = determineWinner(userChoice) # determine the winner

    # add scores
    if winner == "player":
        playerScore += 1
    elif winner == "computer":
        computerScore += 1

    # save scores to file.
    # Alternatively, you could save the score on exit by putting this code in the userChoice == 'exit' conditional.
    # However, this saves the score even if you quit the program without entering exit (for example, by pressing ctrl+c).
    with open('rpsScores.json', 'w') as f:
        json.dump({'player': playerScore, 'computer': computerScore}, f)
    
    # print scores
    print('Player score: ' + str(playerScore) + ' Computer score: ' + str(computerScore), end='\n\n') # 2 newlines to separate the scores from the next round