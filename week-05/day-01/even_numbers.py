# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains only the even numbers.

original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
result = filter(lambda x: x % 2 == 0,original_list)
print(list(result))