# Error Checking 
# Liam Fletcher 
# 14 October 2026

# code that test if a vaild input was given (v1)
'''done = True # Boolean
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

print(f"the number you enterd is {num}")'''

# Using a try and except method to check for valid input.
# Use try and except method to catch errors

done = False 
while not done:
    try:
        num = float(input("please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid number. \n")

print(f"the number you entered is {num}")