# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)
print("Please input numbers:")
input_nums=input()
def print_params(*args):
    print(*args)

print_params(input_nums)