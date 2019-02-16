import random

numberToGuess = random.randint(0,100)

guessing = True

while guessing:
    print(numberToGuess)
    x = int(input('Enter a number: '))
    if(numberToGuess == x):
        print("You got it!! It was: " + numberToGuess)
        break
    if(numberToGuess != x):
        print("Not quite, but you're hot! Keep guessing")

