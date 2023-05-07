# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2023";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Becker - call to function goes here
    jumpTable['3'] = stub                 # Cantu - call to function goes here
    jumpTable['4'] = stub                 # Delgado - call to function goes here
    jumpTable['5'] = stub                 # Garcia Tadeo - call to function goes here
    jumpTable['6'] = stub                 # Gloria - call to function goes here
    jumpTable['7'] = stub                 # Menifee - call to function goes here
    jumpTable['8'] = stub                 # Rountree - call to function goes here
    jumpTable['9'] = stub                 # Stewart - call to function goes here
    jumpTable['10'] = sylvesterFunction                # Sylvester - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Becker")
    print("3.  Cantu")
    print("4.  Delgado")
    print("5.  Garcia Tadeo")
    print("6.  Gloria")
    print("7.  Menifee")
    print("8.  Rountree")
    print("9.  Stewart")
    print("10. Sylvester")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()

# *****************************************************************************************
# FUNCTION:         sylvesterFunction
# DESCRIPTION:      Lets the user play a game of pigdice that is absolutely not rigged at all.
# OUTPUT EXAMPLE:   User agrees to roll the dice by entering 'y'
#                   Program outputs the following:
#                        You rolled a 3!
#
#                        Your Score = 3
#                        Do you want to roll again? (y/n):
# *****************************************************************************************

def sylvesterFunction():
    from random import randint           
    ###############FUNCTION STARTS HERE#####################
    playerTotal = 0
    cpuTotal = 0
    winningValue = 100 #You can use this to determine how long a game is.
    rigValue = 10 #This is how biased it is against the player. The higher the number, the harder the game.
    validInput = ["Y","N"]
    print("Welcome to rigdice!")
    print("Where nothing is suspicious at all!")
    print("First player to reach " + str(winningValue) + " in score wins!")
    print("Be careful! If you roll a 1, your score resets!")
    #####INTRO ENDS HERE#####

    ####KEY LOOP####
    while (cpuTotal < winningValue and playerTotal < winningValue): #Checks to see if a victory has been reached.
            
        ####PLAYER'S TURN####
        playerTries = input("Do you want to roll? (y/n):")
        while(playerTries.upper() not in validInput):
            print("Invalid input! Enter 'Y' to roll or 'N' to pass!")
            playerTries = input("Do you want to roll? (y/n):")
        
        while(playerTries.upper() == 'Y'):
            if playerTotal >= winningValue-rigValue: #Check if the player is close to winning.
                
                #There is now a 1 in 3 chance of losing it all instead of 1 in 6
                riskChance = randint(1,3)
                if riskChance == 1: #The roll is totally rigged at this point.
                    total = 1
                    print("You rolled a " + str(total) + "!\n")
                    playerTotal = 0
                        
                    #Taunt the player for "encouragement"
                    tauntText = ["So close!\n", "Maybe next time.\n", "Almost had it...\n", "You'll get it next time!\n","Maybe one more...\n"]
                    print("You have lost all your points!")
                    print(tauntText[randint(0,4)])
                    break
                
                        ##They passed the test but at this point you can't "roll" higher than a 2.
                else:
                    total = 2
                    print("You rolled a " + str(total) + "!\n")
                    playerTotal = playerTotal + total
                    
                    if playerTotal >= winningValue:
                        #Check if they've finally won
                        print("Your Score = " + str(playerTotal))
                        print("You win!")
                        break
                    
                    else: 
                        print("Your Score = " + str(playerTotal))
                    playerTries = input("Do you want to roll again? (y/n):")
                    
                #The player isn't close to winning yet so play as normal.
            else:
                total = randint(1,6)
                print("You rolled a " + str(total) + "!\n")
                playerTotal = playerTotal + total #Add what they rolled to their total.
                if playerTotal >= winningValue:
                    #Check if they've finally won
                    print("Your Score = " + str(playerTotal))
                    print("You win!")
                    break
                                
                elif total == 1: #If the dice lands on 1, wipe points.
                    playerTotal = 0
                    print("You have lost all your points! \n")
                    break
                
                else: 
                    print("Your Score = " + str(playerTotal))
                    playerTries = input("Do you want to roll again? (y/n):")
                    
            while(playerTries.upper() not in validInput):
                print("Invalid input! Enter 'Y' to roll or 'N' to pass!")
                playerTries = input("Do you want to roll? (y/n):")
            
                
                            
        ####CPU'S TURN####
        if playerTotal < winningValue:
            """Rolls randomly for the cpu when it is the cpu's turn. The CPU has no cheeky bias"""
            cpuTries = randint(1, 10) #The CPU could roll anywhere between 1 to 10 times.
            print("\nComputer is going to roll " + str(cpuTries) +" times.")
            while(cpuTries > 0):
                cpuTries = cpuTries - 1
                total = randint(1,6)
                print("CPU has rolled a " + str(total) + "!")
                cpuTotal = cpuTotal + total
                if cpuTotal >= winningValue:
                    print("Computer Score = " + str(cpuTotal))
                    print("The computer wins!")
                    cpuTries = 0
                    break
                        
                elif total == 1: #If the dice lands on 1, oops it's your turn!
                    cpuTotal = 0
                    print("The computer has lost all its points!")
                    cpuTries = 0
                    
                else: 
                    print("Computer Score = " + str(cpuTotal))
            if cpuTotal < winningValue:
                print("Your turn!\n")
            ####CPU TURN ENDS####    
                
    print("Game over!")
    playerTotal = 0
    cpuTotal = 0
####FUNCTION ENDS HERE#####

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()

