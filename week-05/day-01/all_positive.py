# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether every number is positive or not using all().
original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]


def positive_num(nums):
    return all([num > 0 for num in nums])

print(positive_num(original_list))