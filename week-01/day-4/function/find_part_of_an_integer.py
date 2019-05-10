#  Create a function that takes a number and a list of numbers as a parameter
#  Returns the indeces of the numbers in the list where the first number is part of
#  Or returns an empty list if the number is not part of any of the numbers in the list
# Example
#print(subint(1, [1, 11, 34, 52, 61]))
# should print: `[0, 1, 4]`
#print(subint(9, [1, 11, 34, 52, 61]))
# should print: '[]'

def subint(num,target_list):
    output=[]
    for i in range(len(target_list)):
        if str(num) in str(target_list[i]):
            find_num=int(str(target_list[i]))
            output.append(find_num)
    return output

print(subint(1,[12,45,15]))

