# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether it contains even numbers or not, using any().

original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

def has_even_number(nums):
    return any([num % 2 == 0 for num in nums])

print(has_even_number(original_list))