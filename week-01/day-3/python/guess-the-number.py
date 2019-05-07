# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
store_num = 8
guess_num = 0
while guess_num != store_num:
    guess_num=int(input())
    if guess_num > store_num:
        print("The stored number is lower")
    elif guess_num < store_num:
        print("The stored number is higher")
    else:
        print(f"You found the number: {guess_num}")
