secretNum = 42
maxCount = 10
currentCount = 0
hotBound = 5
userInput = 0


while((currentCount < maxCount) & (userInput != secretNum)):
    userInputUnformatted = input("Guess a number: ") #add check to enforce input to be number
    userInput = int(userInputUnformatted)
    if(userInput == secretNum):
        print("Correct")
        quit()
    print("Incorrect")
    currentCount += 1
    if(abs(userInput - secretNum) <= hotBound):
        print("...but your answer is \"hot\"")
    else:
        print("...your answer is \"cold\"")

if(currentCount >= maxCount):
    print("Game over.")
    quit()
