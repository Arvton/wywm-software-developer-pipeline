import random

# Call for this when you want to create a new knight
def create_knight(knights):

    # Creates a new list for the knight
    knights_data = []

    print("Let's create a knight!")

    # Set the information up for the knight
    knights_data.append(str(input("What is the knight's name? ")))

    # Adds the information to the knight
    knights.append(knights_data)

# Call a knight and change their data
def change_data(knights):

    print("--- What would you like to update? ---")
    print("1: Knight's name: " + knights[0])
    #add different options here for the assignment
    print("0: Retire this knight, Sir " + knights[0] + "\n")
    try:

        selection = int(input("Select your option: "))

        if  selection == 1:
            if knights_number == 0:
                    print("You have a knight!")
            knights[0] = str((input("What is their new name? ")))
            print("Your knight's new name is: " + knights[0])
            return
        elif selection == 0:
            print("Goodbye Sir " + knights[0] + "\n")
            knights.pop(0)
            return

        else:
            print("--- Please select a valid option ---")

    except:
        print("--- Try again! ---")
        change_data(knights)

# Show the current knights and select one
def select_knight(knights):

    # Reset the list to print all the knights
    knights_number = 0
    print("What Knight would you like to update?\n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + " Knight's name: " + str(knights[knights_number][0]))
        knights_number += 1

    selection =(int(input("\nSelect the knight's number: ")) - 1)
    change_data(knights[selection])

# This is the menu and we make our selections here
def menu(knights_number):

    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("0: Exit")

    # Allow a selection to be tested
    try:

        # Takes the user's selection option
        select = int(input("Selection number: "))
        print() # Creates a blank line !!!!!!!!!!!!!!! Look for other ways for the assessment

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            # Print out the Knight that was made
            print("\n--- Your Knight ---\n")
            print("Knight's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select ==2:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
            else:
                select_knight(knights)
            menu(knights_number)
        elif select == 0:
            print("--- All your Knights! ---\n")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + " Knight's name: " + str(knights[knights_number][0]))
                knights_number += 1

            if int(len(knights)) == 0:
                print("Wait... You have no knights! Have a number: " + str(random.randint(0,100)))

        # Required for catching an integer
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)

    # We are looking for an integer selection
    except:
        print("---- Try Again! ----\n")
        menu(knights_number)

# Setting the scene
knights_number = 0
knights = []

# Run the program
menu(knights_number)

#this version gets caught on the except after retiring a knight
#try adding more than one knight before removing a knight -- this makes it fail too and it won't even show