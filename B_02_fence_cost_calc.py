# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
        
    error = "Please enter a nuber that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            responce = float(input(question))

            # check that the number is more than zero
            if responce > 0:
                return responce
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine starts here... 

keep_going = ""
while keep_going == "":

    # Get width and height

    width = num_check(f"Width in M: ")
    length = num_check(f"Length in M: ")
    price = num_check(f"Price per M: ")

    #calculate the perimiter 
    perimiter = 2 * (width + length)
    print(f"The total perimiter of your fence is {perimiter} M's ")

    # calculate the total cost
    totalCost = perimiter * price

    # Output the total cost
    print(f"The cost of your fence is ${totalCost}")

    # ask the user if they want to keep going
    keep_going = input("\nThank you for useing this fence cost calculator. Press enter to keep going or any other key to quit.\n")    