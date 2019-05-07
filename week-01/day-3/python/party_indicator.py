# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people
print("The party is exellent!")
input_num1=int(input())
input_num2=int(input())
total=input_num1+input_num2

if input_num1 == 0:
    print(" ")
else:
    if input_num1 == input_num2 and total >= 20:
        print("Quite cool party")
    elif input_num1 != input_num2 and total >= 20:
        print("Average party")
    elif total < 20:
        print("Sauage party")

