# Hi
# Semester 2 Year 10 DGT 2026 Demo code
# Author: Liam Fletcher
# Date 16/09/2026
# Version: 1

# Demistation of how a while loop works
# and how intending affects the code
'''keep_going = ""
while keep_going == "":
    print("looping")
    print("still looping...")

    keep_going = input("Do you want to keep going?")

print("all done") '''

# demonstarting error catching 
keep_going = ""
while keep_going == "":

    try: 
        response = int(input("Number: "))
        print("You enterd an integer.")

    except ValueError:
        print("Yikes! That is not an integer. Please try again.")

    keep_going = input("Again?")

print("All done. Thanks")
