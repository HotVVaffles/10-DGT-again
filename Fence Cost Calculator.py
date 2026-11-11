# Date: November 11 2026
# Author: Liam Fletcher
# Title : Fence Cost Calculator
# Version: 1


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
            print("The measurement must be JUST a number")

def num_check(question):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print("Reminder that the number MUST be greater than zero")

        except ValueError:
            print("The measurement must be JUST a number")

def num_check(question):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print("Reminder that the number MUST be greater than zero")

        except ValueError:
            print("The cost must be JUST a number")


while True:
    for item in range(1):
        width = num_check("What is the width: ")
        

    print()

    for item in range(1):
        height = num_check("What is the length: ")
        

    print()
    for item in range(1):
        unit = (num_check("What is the cost per meter? "))

    print()
    perimeter = 2 * (width + height)
    print(f"The perimeter of your fence is {perimeter} ")
    cost = perimeter * unit
    print(f"The cost of the fence in total is ${cost} ")
    print()
    again = input("Again? (y/n): ")
    print()
    if again not in ('Y', 'y', 'Yes', 'yes'):
        print("I hope I've helped you with your caulculations. \nHave a great day!")
        break
  