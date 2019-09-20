import random

ComputerNumber = random.randint(1,1000000)
GameOver = False
guessNumber = 0
lowRange = 1
highRange = 1000000

#this is the game loop
while not GameOver:
    print("Enter an integer")
    print(highRange, lowRange)
    playerGuess = input()
    x = int(playerGuess)
    guessNumber = guessNumber + 1
    print (guessNumber)
    if x == ComputerNumber:
        print ("you win")
        GameOver = True
    elif guessNumber == 20:
        print("you lose")
        print ("the correct number is", ComputerNumber)
        GameOver = True
    elif x > highRange:
        print ("out of range")
        guessNumber = guessNumber - 1
        print (highRange, lowRange)
    elif x < lowRange:
        print ("out of range")
        print (highRange, lowRange)
    elif x > ComputerNumber:
        print ("sorry too high")
        print ("adjusting range")
        highRange = x
        print(highRange, lowRange)
    elif x < ComputerNumber:
        print ("sorry too low")
        print ("adjusting range")
        lowRange = x
        print (highRange, lowRange)
        
        
