# Michael DeVito II
# pig_v4.py OR two_dice_pig.py
# A dice game called "Pig" now with user and CPU battling it out. AND two dice pig and big pig variations!

from random import randrange  
from time import * # I added pauses in the code to make things smoother and make it so text doesn't appear at lightning speed
import os # I wanted to try clearing the terminal after every few rounds so that the terminal doesn't overflow with text.

def roll():
    return randrange(6) + 1

def takeTurnCPU(holdAmount,bigPig):
    rollNumber,turnScore,doubleOnes = 0,0,False # initialize local variables
    while turnScore <= holdAmount:
        rollNumber += 1
        roll1,roll2 = roll(), roll() # troubleshooting, should both be roll()
        if roll1 == 1 and roll2 == 1:
            if bigPig == True:
                turnScore += 25
                print(f"CPU has hit Big Pig! +25 points")
            elif bigPig == False:
                print("Oh no! The CPU rolled two 1s and lost their score!")
                turnScore = 0
                doubleOnes = True
                break
            else:
                print("Something went wrong! (Error Code: ROLL_CHECK_CPU)")
                break
        elif roll1 == roll2 and bigPig == True:
            print("The CPU got doubles! Point value for that roll was doubled.")
            turnScore += ((roll1 + roll2) * 2)
        elif roll1 == 1 or roll2 == 1:
            turnScore = 0
            break
        else:
            turnScore += roll1 + roll2
    sleep(0.5)
    print(f"CPU scored {turnScore} points after {rollNumber} rolls")
    return turnScore, doubleOnes

def takeTurnInteractive(playerScore,CPUscore,bigPig):
    turnScore,rollNumber,keepPlay,doubleOnes = 0,1,True,False # initialize local variables
    while keepPlay == True:
        roll1,roll2,answer = roll(),roll()," " 
        print(f"\n-- Roll number {rollNumber} --")
        sleep(0.25)
        print(f"You Rolled: {roll1} & {roll2}")
        sleep(0.25)
        if roll1 == 1 and roll2 == 1:
            if bigPig == True:
                turnScore += 25
                print(f"You hit Big Pig! +25 points")
                sleep(0.25)
            elif bigPig == False:
                print("Oh no! You rolled two 1s and lost your score!")
                turnScore = 0
                doubleOnes = True
                sleep(0.25)
                break
            else:
                print("Something went wrong! (Error Code: ROLL_CHECK_PLAYER)")
                break
        elif roll1 == roll2 and bigPig == True:
            print("You got doubles! Point value for that roll was doubled.")
            turnScore += ((roll1 + roll2) * 2)
        elif roll1 == 1 or roll2 == 1:
            print("Score for this turn set to 0.")
            turnScore = 0
            break
        else:
            turnScore += roll1 + roll2
        print(f"Score for this turn is now {turnScore}")
        print(f"Your total score: {playerScore + turnScore}     CPU total score: {CPUscore}")
        answer = str(input("Would you like to roll again? (y/n) "))
        if answer.lower() == "n":
            keepPlay = False
        elif answer.lower() == "y":
            rollNumber +=1
            keepPlay = True
        else:
            print("Something went wrong. Please try again! (Exit Code: TAKETURNINTERACTIVE)")
            break
    sleep(0.25)
    return turnScore,doubleOnes
            
        

def main():
       try: # try everything in main()

        # Code from Previous Iterations:
        # amount = int(input("Enter a positive integer value for holdAmount: "))
        # turnNumber = 1
        # print("\nCPU begins turn #",turnNumber)
        # print("Total score for this turn:", takeTurn(amount),"\n")
        # input("Pig: The Dice Game\nPress any key to start.")
        # takeTurnInteractive()
        regularInstructions = {
            "Welcome to the dice game Pig! Here are the instructions on how to play:\n"
            "1. Each turn, a player rolls two die until the player decides to 'hold.'\n"
            "2. Each time you roll, you add the numbers on the die to your score.\n"
            "3. However, if you roll a 1 on either die, your score for that round becomes 0.\n"
            "4. When you hold, your score for that round is saved and added to your total score across all rounds.\n"
            "5. The first player to reach 100 wins!\n"
            "Note: In this version, you get to decide what the CPU's hold amount is. A good hold score for the CPU in Two-Die Pig is anywhere from 10-30.\n"
        }
        bigPigInstructions =  {
            "These are the special rules for the Big Pig variant of Pig:\n"
            "1. If two 1s are rolled, the player adds 25 to his or her turn total.\n"
            "2. If other doubles are rolled (example: two 4s) the player adds twice the value of the dice to his or her turn total.\n"
        }

        for i in regularInstructions:
            print(i)
        for i in bigPigInstructions:
            print(i)

        round,playerScore,CPUscore,turnScore,doubleOnes,bigPig,play = 1,0,0,0,0,False,True # initializing variables
        try: # try to get inputs
            amount = int(input("What should the CPU's hold amount be? Enter a positive integer: "))
            answer = str(input("Would you like to play with the Big Pig variation? (y/n) "))
            if answer.lower() == "y":
                bigPig = True      
                input("Big Pig has been activated! Press any key to begin.")
            elif answer.lower() == "n":
                bigPig = False
                input("Big Pig has been deactivated. Press any key to begin.")
            else:
                print("Something went wrong! Defaulting to no Big Pig. (Error Code: INPUT_BIGPIG)")
                input("Press any key to begin.")
            os.system('cls' if os.name == 'nt' else 'clear') # source 1 aided with this line
            if bigPig == True:
                print(f"\nBegin Two-Dice Pig with Big Pig! First player to 100 wins!")
            else:
                print(f"\nBegin Two-Dice Pig! First player to 100 wins!")
        except: # if someone inputs the wrong thing
            print("Something went wrong! Please try again. (Exit Code: INPUTS)")
            play = False
            input("Press <Enter> to end.")
        while play == True: # main game loop
            print(f"\n------- Round {round}: CPU -------")
            turnScore,doubleOnes = takeTurnCPU(amount,bigPig)
            CPUscore += turnScore
            if doubleOnes == True:
                CPUscore = 0
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
            turnScore,doubleOnes = takeTurnInteractive(playerScore,CPUscore,bigPig)
            playerScore += turnScore
            if doubleOnes == True:
                playerScore = 0
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