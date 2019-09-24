import random

#these are the rules of the game
ComputerNumber = random.randint(1,1000000)
GameOver = False
guessNumber = 0
lowRange = 1
highRange = 1000000
print("guess a number between one and a million")
#this is the game loop
while not GameOver:
    print(highRange,lowRange)
    playerGuess = input("enter an integer:")
    x = int(playerGuess)
    guessNumber = guessNumber + 1
    print (guessNumber)
    if x == ComputerNumber:
        print ("you guessed the correct number")
        print ("you win!")
        GameOver = True
    elif guessNumber == 20:
        print("you lose:(")
        print ("the correct number is", ComputerNumber)
        GameOver = True
    elif x > highRange:
        print ("out of range")
        guessNumber = guessNumber - 1
    elif x < lowRange:
        print ("out of range")
    elif x > ComputerNumber:
        print ("sorry too high")
        print ("adjusting range")
        highRange = x
    elif x < ComputerNumber:
        print ("sorry too low")
        print ("adjusting range")
        lowRange = x
