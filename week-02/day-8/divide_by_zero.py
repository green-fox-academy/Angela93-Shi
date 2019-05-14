# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

def divide_by_zero():
    parameter = int(input())
    try:
        result = 10 / parameter
        print(result)
    except ZeroDivisionError:
        print("failed,the parameter can\'t be zero")
    finally:
        print("completed")

divide_by_zero()
