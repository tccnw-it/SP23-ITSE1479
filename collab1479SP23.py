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
    jumpTable['9'] = stewartFunction      # Stewart - call to function goes here
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
# FunctionName:  stewartFunction
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stewartFunction 
# DESCRIPTION:      A function that creates a password based on the user's last name, 
#                   birth city, and phone number as input.
#                   It then prints out a concatenation of the last 4 letters of the 
#                   last name reversed, a special character based on the first letter of the birth city, 
#                   and the sum of all the numbers of the phone number divided by 
#                   7 and multiplied by 63. 
# OUTPUT EXAMPLE:   Stewart, Fort Worth, and 8172368151 would turn into traw;735513133590
# *****************************************************************************************
def stewartFunction():
    print("*" * 30)
    print("* Strong Password Generator")
    print("*" * 30)

    print("Enter the following information")
    print("_" * 20)
    lName = input("Last name:")
    bCity = input("Birth city:")
    pNum = input("Phone number (numbers only):")
    newP = 0

    bCity = bCity.lower()
    if (bCity[:1] =='a' or bCity[:1] =='e' or bCity[:1] =='i' or bCity[:1] =='o' or bCity[:1] =='u'):
        newCity = ":"
    elif (bCity[:1] < "n"):
        newCity = ";"
    elif (bCity[:1] >= "n"):
        newCity = "!"

    for i in range (10):
        newP += int(pNum[i])

    newP = (newP / 7) * 63

    print("Your strong password is: {l}{b}{p}".format(l = lName[:-5:-1], b = newCity, p = int(newP)))
    print("Program complete.")


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
