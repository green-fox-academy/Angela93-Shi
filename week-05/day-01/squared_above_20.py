# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains the numbers if their squared value is above 20.
original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
result = map(lambda x: x ** 2,original_list)
list_above_20 = filter(lambda x:x>20,result)
print(list(list_above_20))