# Michael DeVito II
# pig_v2.py
# A dice game called "Pig" now with user playing!

from random import randrange  
import time # I added pauses in the code to make things smoother and make it so text doesn't appear at lightning speed

def roll():
    return randrange(6) + 1

def takeTurn(holdAmount):
    turnScore = 0

    while turnScore <= holdAmount:
        rollAmount = roll()
        print("CPU Rolled:", rollAmount)
        if rollAmount == 1:
            print("Score for this turn set to 0.")
            turnScore = 0
            break
        else:
            turnScore += rollAmount

    return turnScore

def takeTurnInteractive():
    turnScore = 0
    turnNumber = 1
    keepPlay = True

    while keepPlay == True:
        rollAmount = roll()
        print("\n----- Begin turn number", turnNumber, "-----")
        time.sleep(0.25)
        print("You Rolled:", rollAmount)
        time.sleep(0.25)
        if rollAmount == 1:
            print("Score for this turn set to 0.")
            turnScore = 0
            break
        else:
            turnScore += rollAmount
            print("Score for this turn is now", turnScore)
        
        x = str(input("Would you like to roll again? (y/n) "))
        if x.lower() == "n":
            keepPlay = False
        elif x.lower() == "y":
            turnNumber +=1
            keepPlay = True
        else:
            print("Something went wrong. Please try again!")
            break

    time.sleep(0.25)
    print("\nTotal score after", turnNumber, "turns:", turnScore)
            
        

def main():
    # Add code here to test the takeTurn function.
    try:
        # amount = int(input("Enter a positive integer value for holdAmount: "))
        # turnNumber = 1
        # print("\nCPU begins turn #",turnNumber)
        # print("Total score for this turn:", takeTurn(amount),"\n")
        input("Pig: The Dice Game\nPress any key to start.")
        takeTurnInteractive()

    except:
        print("Something went wrong! Please try again.")
        input("Press <Enter> to end.")

if __name__ == "__main__":
    main()