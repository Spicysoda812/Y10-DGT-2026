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


# main routine goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

    print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
