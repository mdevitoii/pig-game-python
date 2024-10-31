# Michael DeVito II
# pig_v1.py
# A single-turn dice game called "Pig"


from random import randrange  # Needed for roll function.

# Simulate roll of a 6-sided die.  Returns uniformly
# distributed random integer between 1 and 6, inclusive.
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

def main():
    # Add code here to test the takeTurn function.
    try:
        amount = int(input("Enter a positive integer value for holdAmount: "))
        turnNumber = 1
        print("\nCPU begins turn #",turnNumber)
        print("Total score for this turn:", takeTurn(amount),"\n")
    except:
        print("Something went wrong! Please try again.")
        input("Press <Enter> to end.")

if __name__ == "__main__":
    main()