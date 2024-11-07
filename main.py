# -- Guess The Number --
# input player name
# input the lowest integer number
# input the highest integer number
# Program picks a number at random from within that range.
# input guess, Program responds in one of 3 ways Correct, Too high or Too Low.
# Correct: The guess is equal to the number chosen by the program
# Too High: The number guessed is higher than the number selected by the program
# Too Low: The number guessed is Lower than the number selected by the program
# --- Ideas for expansions ---
# Computer player, set to guess random numbers in range of too high and too low from its prior attempts
# add a "would you like to play again" prompt
# -- Guess The Number --
import time
import random

# Set variables
guessCounter = 0
lowValue = 0
highValue = 100
tooLowValue = lowValue
tooHighValue = highValue
chosenNumber = 0
guessedNumber = 2
numberList = []
binarySearchCount = 0
easyMode = False
computerPlayer = False
computerGuess = 0
computerGuessCounter = 0


def valueinput(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")





# obtain low and high values for range
def define_range():
    lowValue = valueinput("Please enter a number to use as the lowest value in the range to guess\n")
    highValue = valueinput("Please enter a number to use as the highest value in the range to guess\n")
    totalRange = highValue - lowValue
    if lowValue < highValue and highValue - lowValue > 100:
        print(f"you have chosen to guess a number between {lowValue} and "
            f"{highValue}\n there are {totalRange} possible numbers to choose from.")
    elif lowValue < highValue and highValue - lowValue < 100:
        print(f"Between {lowValue} and {highValue}\n there are only {totalRange} "
            f"possible numbers to choose from. I am adding 100 to the highest number to make the game more interesting.")
        highValue += 100
    elif lowValue > highValue:
        print(f"The values you entered are not able to be used. The highest value number should be higher "
            f"than the lowest value number using 1 through 1000 instead.")
        lowValue = 1
        highValue = 1000
    return lowValue, highValue


def choose_number(lowValue, highValue):
    chosenNumber = random.randint(lowValue, highValue)
    guessedNumber = 0
    if chosenNumber == 0:
        guessedNumber = 1
    return chosenNumber, guessedNumber


def number_list_generator(lowValue, highValue):
    for x in range(lowValue, highValue + 1):
        numberList.append(x)
    return numberList


def binary_search(chosenNumber,numberList):
    binarySearch = numberList[(len(numberList)) // 2]
    binarySearchCount = 1
    while binarySearch != chosenNumber:
        binarySearchCount += 1
        binarySearch = numberList[(len(numberList)) // 2]
        if binarySearch < chosenNumber:
            numberList = [n for n in numberList if n > binarySearch]
        elif binarySearch > chosenNumber:
            numberList = [n for n in numberList if n < binarySearch]
    return binarySearchCount


def gameplay(chosenNumber, guessedNumber, tooLowValue, tooHighValue, guessCounter, computerGuess, computerGuessCounter, easyMode):
    while chosenNumber != guessedNumber and chosenNumber != computerGuess:
        print(f"Please choose a number between {lowValue} and {highValue}.")
        if computerPlayer == True and guessCounter >= 1:
            computerGuessCounter += 1
            computerGuess = random.randint(tooLowValue, tooHighValue)
            print("ComputerGuess:",computerGuess)
            print("computerGuessCounter:",computerGuessCounter)
            if computerGuess == chosenNumber:
                break
            time.sleep(1)
        if easyMode == True and guessCounter > 0:
            print(f"EASY MODE>> You are looking for a number between: {tooLowValue} and {tooHighValue} ")
        guessedNumber = valueinput("Please guess a number")
        if guessedNumber not in range(lowValue, highValue + 1):
            print(f"You have guessed a number that is outside of the range.")
        elif guessedNumber < chosenNumber:
            print(f"{guessedNumber} is too low")
            if guessedNumber >= tooLowValue:
                tooLowValue = guessedNumber
            guessCounter += 1
            print(f"Total guesses so far: {guessCounter}")
        elif guessedNumber > chosenNumber:
            print(f"{guessedNumber} is too high")
            if guessedNumber <= tooHighValue:
                tooHighValue = guessedNumber
            guessCounter += 1
            print(f"Total guesses so far: {guessCounter}")
        elif guessedNumber == chosenNumber:
            print(f"{guessedNumber} is right! You have won!")
            print(f"You guessed the right number in {guessCounter} attempts")
    if computerPlayer and computerGuess == chosenNumber:
        print("The computer player has guessed the correct number.")
        winner = "computer"
    elif not computerPlayer:
        winner = "player"
    elif computerPlayer and computerGuess != chosenNumber:
        print("You have guessed the correct number before the computer!")
        winner = "player"
    return guessCounter, computerGuess, computerGuessCounter, winner


def determine_score(binarySearchCount, guessCounter, computerPlayer, winner):
    if winner == "computer":
        print("The computer won")
        time.sleep(1)
        print("You did not earn any points this time.")
    elif winner == "player":
        print(f"using the binary search method the program would have guessed the right number in "
              f"{binarySearchCount} guesses.")
        print(f"You won in {guessCounter} guesses")
        time.sleep(1)
        print(f"Calculating your score...")
        time.sleep(1)
        perfectScore = binarySearchCount
        match guessCounter:
            case guessCounter if guessCounter < perfectScore:
                print("110 points, Amazing! better than the computer could do!")
            case guessCounter if guessCounter == perfectScore:
                print("100 points, perfect score!")
            case guessCounter if guessCounter == perfectScore + 1:
                print("90 points")
            case guessCounter if guessCounter == perfectScore + 2:
                print("80 points")
            case guessCounter if guessCounter == perfectScore + 3:
                print("70 points")
            case guessCounter if guessCounter == perfectScore + 4:
                print("60 points")
            case guessCounter if guessCounter == perfectScore + 5:
                print("50 points")
            case guessCounter if guessCounter == perfectScore + 6:
                print("40 points")
            case guessCounter if guessCounter == perfectScore + 7:
                print("30 points")
            case guessCounter if guessCounter == perfectScore + 8:
                print("20 points")
            case guessCounter if guessCounter == perfectScore + 9:
                print("10 points")
            case guessCounter if guessCounter == perfectScore + 10:
                print("5 points")
            case guessCounter if guessCounter > perfectScore + 10:
                print("1 point")


def game_mode():
    easyModeChoice = input(f"would you like easy mode turned on? Y or N ")
    if easyModeChoice.lower() == "y":
        print("Easy mode has been enabled")
        easyMode = True
    else:
        print("Easy mode is not enabled")
        easyMode = False
    time.sleep(1)
    computerPlayerChoice = input(f"would you like to play against the Computer? Y or N ")
    if computerPlayerChoice.lower() == "y":
        print("Computer player enabled")
        computerPlayer = True
    else:
        print("Computer player is not enabled")
        computerPlayer = False
    return easyMode, computerPlayer


playerName = input("Enter Player Name\n")
print(f"Thank you, {playerName} for playing guess the number.")


easyMode, computerPlayer = game_mode()
lowValue, highValue = define_range()
chosenNumber, guessedNumber = choose_number(lowValue, highValue)
tooLowValue = lowValue
tooHighValue = highValue
numberList = number_list_generator(lowValue, highValue)
binarySearchCount = binary_search(chosenNumber, numberList)
guessCounter, computerGuess, computerGuessCounter, winner = gameplay(chosenNumber, guessedNumber, tooLowValue, tooHighValue, guessCounter, computerGuess, computerGuessCounter, easyMode)
time.sleep(3)
determine_score(binarySearchCount, guessCounter, computerPlayer, winner)


exit()
