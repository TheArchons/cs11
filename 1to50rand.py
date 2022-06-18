import random

magic_number = random.randrange(1,51)
guess = int(input("Guess the number I'm thinking of: ")) 
counter = 0

while guess != magic_number and counter < 4: 
    if guess < magic_number:
        guess = int(input("Too low! Guess again: ")) 
    elif guess > magic_number:
        guess = int(input("Too high! Guess again: ")) 
    counter += 1

if guess == magic_number:
    print("You got it in {} guesses! It was {}.".format(counter,magic_number))
else:
    print("You didn't get it in 5 guesses. It was {}.".format(magic_number))
