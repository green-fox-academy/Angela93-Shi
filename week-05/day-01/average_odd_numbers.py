# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the average of the odd numbers.
original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

odd_numbers=list(filter(lambda x:x%2 != 0,original_list))
# average_num = list(map(lambda idx: sum(idx)/float(len(idx)), odd_numbers))
# print(average_num)

def average(inx):
    average_num = sum(inx) / float(len(inx))
    return average_num

print(average(odd_numbers))


