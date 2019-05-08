# Write a function called `sum` that returns the sum of numbers from zero to the given parameter
given_num=10
def sum(num):
    global given_num
    for i in range(num+1):
        given_num=i+given_num
    print(given_num)

sum(given_num)