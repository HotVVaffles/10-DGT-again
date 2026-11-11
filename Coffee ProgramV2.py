# Creating a coffee program so that a user will be able to interact with.
# Liam Fletcher
# 23 September 2026
# Version 1

# TODO: Record an input (store the answer)
#    Check for valid answer (Input checker)
#    Ask Questions and respond 

# Version 1
# Ask the user wether they like coffee or not
'''like_coffee = input("Do you like coffee? (Yes or No)      ")
# print(like_coffee) #checking the input is stored
print(f"Your answer was {like_coffee}")

# Check the input and respond accordingly
if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "YES" or like_coffee == "Y" or like_coffee == "y":
    print("That is great! I like coffee too!")
else:
    print("You are missing out! Why not give it a try? ")'''

# Version 2
# Adding a While Loop to test the program
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? (Yes or No)      ")
    # print(like_coffee) #checking the input is stored
    print(f"Your answer was {like_coffee}")

    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "YES" or like_coffee == "Y" or like_coffee == "y":
        print("That is great! I like coffee too!")
        keep_going = "exit"
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "NO" or like_coffee == "N" or like_coffee == "n":
        print("You are missing out! Why not give it a try? ")
        print("Trust me drinking coffee offers several proven health benefits, including enhanced mental alertness, liver protection, and a lower risk of chronic diseases.")
        print("So, why not give it a try and come back to me later?")
        keep_going = "Convinced"
    else:
        print("That is not a valid answer, please try again.")
