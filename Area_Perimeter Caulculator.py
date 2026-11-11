# Date: October 21st & 23rd
# Author: Liam Fletcher
# Title : Area/Perimeter Calculator
# Version: 1

#lesson 2
'''# Code to learn about variables...

# Variables can be a string
greeting = "Hello, World!"

# Variables can be a number
fav_number = 7

# Variables can be a boolean
love_programing = True

# This variable has a problem
# my name = "John Doe"

print(greeting) 
print(fav_number)
print(love_programing)

my_name = "John Doe" '''

# lesson 3
'''
# ask the user for their name

# ask the user for their favourite number (interger)

# Double, halve, and square the favourite number

# Greet the user

# Output the results of doubling, halving, 
# and squaring the favourite number

username = input("What is your name? ")
fave_number = (int(input("What is your favourite number? ")))
double = fave_number * 2
half = fave_number / 2
square = fave_number ** 2
print(f"Hi {username}, your favourite number is {fave_number}")

print(f"Double {fave_number} is {double},")
print(f"Half {fave_number} is {half},")
print(f"And {fave_number} squared is {square}")
print()
print(f"Have a nice day {username}")'''

#lesson 4 & 5

'''# ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):


    error = "please enter an number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

#main rountine goes here
for item in range(0, 2):
    width = num_check("width:  ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height:  ")
    print(height)'''

# lesson 6

print()
print("Please keep in mind that any measurements you enter must be over zero. Thank you")
print()
def num_check(question):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print("Reminder that the number MUST be greater than zero")

        except ValueError:
            print("The measurement must be JUST a number, wait to tell me the unit soon")

def num_check(question):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print("Reminder that the number MUST be greater than zero")

        except ValueError:
            print("The measurement must be JUST a number, wait to tell me the unit soon")


while True:
    for item in range(1):
        width = num_check("What is the width: ")
        

    print()

    for item in range(1):
        height = num_check("What is the height: ")
        

    print()
    unit = (input("What is the unit of measure? (mm, cm, m, or km)  "))

    print()
    perimeter = 2 * (width + height)
    print(f"The perimeter of this object is {perimeter} {unit}")
    area = width * height
    print(f"The area of this object is {area} {unit}² ")
    print()
    again = input("Again? (y/n): ")
    print()
    if again not in ('Y', 'y', 'Yes', 'yes'):
        print("I hope I've helped you with your caulculations. \nHave a great day!")
        break
  