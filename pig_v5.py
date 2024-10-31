# Michael DeVito II
# pig_v5.py
# A dice game called "Pig" now with user and CPU battling it out! AND with CPU strategy!

from random import randrange  
from time import * # I added pauses in the code to make things smoother and make it so text doesn't appear at lightning speed
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
 # hello! testing github
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
    try:    
        regularInstructions = {
            "Welcome to the dice game Pig! Here are the instructions on how to play:\n"
            "1. Each turn, a player rolls a die until the player decides to 'hold.'\n"
            "2. Each time you roll, you add the numbers on the die to your score.\n"
            "3. However, if you roll a 1 on the die, your score for that round becomes 0.\n"
            "4. When you hold, your score for that round is saved and added to your total score across all rounds.\n"
            "5. The first player to reach 100 wins!\n"
        }
        for i in regularInstructions:
            print(i)

        round,playerScore,CPUscore,turnScore,play = 1,0,0,0,True # initializing variables
        try: # try to get inputs
            amount = int(input("What should the CPU's hold amount be? Enter a positive integer: "))      
            os.system('cls' if os.name == 'nt' else 'clear') # source 1 aided with this line
            print(f"\nBegin Two-Dice Pig! First player to 100 wins!")
        except: # if someone inputs the wrong thing
            print("Something went wrong! Please try again. (Exit Code: INPUTS)")
            play = False
            input("Press <Enter> to end.")
        while play == True: # main game loop
            print(f"\n------- Round {round}: CPU -------")
            turnScore = takeTurnCPU(amount)
            CPUscore += turnScore
            sleep(.25)
            print(f"CPU Total Score: {CPUscore}")
            sleep(.25)
            print(f"Player Total Score: {playerScore}")
            if CPUscore >= 100:
                input("\nLooks like the CPU won this game! Thank you for playing.\nPress any key to exit.")
                break
            elif playerScore >= 100:
                input("\nLooks like you won this game! Thank you for playing. \nPress any key to exit.")
                break
            print(f"\n------- Round {round}: Player -------")
            turnScore = takeTurnInteractive(playerScore,CPUscore)
            playerScore += turnScore
            if CPUscore >= 100:
                input("\nLooks like the CPU won this game! Thank you for playing.\nPress any key to exit.")
                break
            elif playerScore >= 100:
                input("\nLooks like you won this game! Thank you for playing. \nPress any key to exit.")
                break
            input(f"Press <Enter> to continue to round {round+1}.")
            if round % 2 == 0:
                os.system('cls' if os.name == 'nt' else 'clear') # source 1 aided with this line
            round += 1
    except: # error checking
        print("Something went wrong! Please try again. (Exit code: MAIN)")
        input("Press <Enter> to end.")

if __name__ == "__main__":
    main()


##### REFERENCES #####
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
# - used for help with clearing the terminal every few rounds so that the terminal doesn't flood