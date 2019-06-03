# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the sum of the even numbers which are below or equal to 10.

original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

result= sum(list(filter(lambda x:x % 2 ==0 and x <= 10,original_list)))
print(result)