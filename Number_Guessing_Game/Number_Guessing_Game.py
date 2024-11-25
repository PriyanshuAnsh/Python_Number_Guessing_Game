import random

randomNumber: int = int(random.random() * 10)
tries = 3
while(tries != 0):
    guessedNumber: int = int(input("Guess the Number? "))
    if(guessedNumber == randomNumber):
        print("Cool! You Won In", 4 - tries, "attempts!")
        break
    else:

        if(guessedNumber > randomNumber):
            print("You Guessed High!")
        else:
            print("You Guessed Low!")
        tries -= 1
        print("Good Luck Next Try!\n"
              "Tries Left: ", tries)
if(tries == 0):
    print("Alas! The Number was: ", randomNumber)