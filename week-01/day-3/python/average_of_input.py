# Write a program that asks for 5 integers in a row
# then it should print the sum and the average of these numbers like:
# Sum: 22, Average: 4.4
total = 0
average =0
for i in range(5):
    input1=int(input())
    total+=input1
    average=total/input1
print("Sum:"+str(total)+","+"Average:"+str(average))