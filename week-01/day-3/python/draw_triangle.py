# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

input_num = int(input())
for i in range(input_num):
    print("*" * i)