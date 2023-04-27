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
    jumpTable['2'] = beckerFunction       # Becker - call to function goes here
    jumpTable['3'] = stub                 # Cantu - call to function goes here
    jumpTable['4'] = stub                 # Delgado - call to function goes here
    jumpTable['5'] = stub                 # Garcia Tadeo - call to function goes here
    jumpTable['6'] = stub                 # Gloria - call to function goes here
    jumpTable['7'] = stub                 # Menifee - call to function goes here
    jumpTable['8'] = stub                 # Rountree - call to function goes here
    jumpTable['9'] = stub                 # Stewart - call to function goes here
    jumpTable['10'] = stub                # Sylvester - call to function goes here

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
def beckerFunction():
    totalPoints = 0
    numGrades = 0
    letterGrade = "Undefined"

    print("\nPlease enter grades you would like to have averaged.")
    grade = input ("\nEnter grades(0-100) one at a time (hit enter to submit). Enter \"Q\"  when you have entered all grades you wish to enter.")
    while grade != "Q":
        if int(grade) >= 0 and int(grade) <= 100:
            totalPoints += int(grade)
            numGrades += 1
            if int(grade) >= 90 and int(grade) <= 100: letterGrade = "A"
            elif int(grade) >= 80 and int(grade) <= 89: letterGrade = "B"
            elif int(grade) >= 70 and int(grade) <= 79: letterGrade = "C"
            elif int(grade) >= 60 and int(grade) <= 69: letterGrade = "D"
            elif int(grade) < 60: letterGrade = "F"
            print ("A(n) " + grade + " is a(n) " + letterGrade + ".")
            grade = input ("Please enter a grade between zero and 100. Type \"Q\" when you have entered all grades.")
        else:
            grade = input("There was an error. \"Please enter a grade between zero and 100. ")
    if numGrades > 0:
        print ("\nThank you. The average of all entered grades, excluding errors was: " + str(round(totalPoints/numGrades)))
    else:
        print ("\nYou did not entered any grades. No average available." )

    print("\nPress ENTER to continue.")
    input()   

def stub():
    print()
    print()

    
    print("Press ENTER to continue.")
    input()   

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