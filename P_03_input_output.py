# Ask user for their name
username = input("What is your name? ")
# Ask usser for their favorite number (intiger)

fav_number = int(input("What is your favorite number? "))

# Double, halve and square the users number 
double = fav_number * 2
halve = fav_number / 2
square = fav_number * fav_number

# Greet the user
print()
print(f"Hi {username}, your favortite number is {fav_number}")

# Output the results of doubling, halving and 
# squaring their favorite intiger
print(f"Double {fav_number} is {double}.")
print(f"Half {fav_number} is {halve}")
print (f"{fav_number} squared is {square}")
print()
print("Have a nice day.")
 
