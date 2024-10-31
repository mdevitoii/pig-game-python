# Michael DeVito II
# pig_v3.py
# A dice game called "Pig" now with user and CPU battling it out!

from random import randrange  
import time # I added pauses in the code to make things smoother and make it so text doesn't appear at lightning speed
import os # I wanted to try clearing the terminal after every few rounds so that the terminal doesn't overflow with text.

def roll():
    return randrange(6) + 1

def takeTurnCPU(holdAmount):
    rollNumber = 0
    turnScore = 0

    while turnScore <= holdAmount:
        rollNumber += 1
        rollAmount = roll()
        if rollAmount == 1:
            turnScore = 0
            break
        else:
            turnScore += rollAmount
    time.sleep(0.5)
    print(f"CPU scored {turnScore} points after {rollNumber} rolls")
    return turnScore

def takeTurnInteractive(playerScore,CPUscore):
    turnScore = 0
    rollNumber = 1
    keepPlay = True

    while keepPlay == True:
        rollAmount = roll()
        print("\n-- Roll number", rollNumber, "--")
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
            print(f"Your total score: {playerScore + turnScore}     CPU total score: {CPUscore}")
        
        x = str(input("Would you like to roll again? (y/n) "))
        if x.lower() == "n":
            keepPlay = False
        elif x.lower() == "y":
            rollNumber +=1
            keepPlay = True
        else:
            print("Something went wrong. Please try again! (Exit Code: TAKETURNINTERACTIVE)")
            break

    time.sleep(0.25)
    return turnScore
            
        

def main():
    # Add code here to test the takeTurn function.
      # try:
        # amount = int(input("Enter a positive integer value for holdAmount: "))
        # turnNumber = 1
        # print("\nCPU begins turn #",turnNumber)
        # print("Total score for this turn:", takeTurn(amount),"\n")
        # input("Pig: The Dice Game\nPress any key to start.")
        # takeTurnInteractive()
        amount = int(input("What should the CPU's hold amount be? "))
        round = 1
        playerScore = 0
        CPUscore = 0
        print("\nWelcome to Pig! First player to 100 wins!")
        while True:
            print(f"\n------- Round {round}: CPU -------")
            CPUscore += takeTurnCPU(amount)
            time.sleep(.25)
            print(f"CPU Total Score: {CPUscore}")
            time.sleep(.25)
            print(f"Player Total Score: {playerScore}")
            print(f"\n------- Round {round}: Player -------")
            playerScore += takeTurnInteractive(playerScore,CPUscore)
            if CPUscore >= 100:
                input("\nLooks like the CPU won this game! Thank you for playing.\nPress any key to exit.")
                break
            elif playerScore >= 100:
                input("\nLooks like you won this game! Thank you for playing. \nPress any key to exit.")
                break
            input(f"Press <Enter> to continue to round {round+1}.")z
            if round % 3 == 0:
                os.system('cls' if os.name == 'nt' else 'clear') # this line is taken directly from source 1
            round += 1
            
        


      # except:
            # print("Something went wrong! Please try again. (Exit code: MAIN)")
            # input("Press <Enter> to end.")

if __name__ == "__main__":
    main()



##### REFERENCES #####
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
# - used for help with clearing the terminal every few rounds so that the terminal doesn't flood