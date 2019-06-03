# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains the positive items' squared value.
original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
positive_nums = list(filter(lambda x: x>0,original_list))
result = map(lambda x: x ** 2,positive_nums)
print(list(result))