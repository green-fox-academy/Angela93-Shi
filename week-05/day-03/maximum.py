# Write a function that finds the largest element of an array using recursion.

def maximum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0],maximum(arr[1:]))

arr = input("Enter an array:")
result = maximum(arr)
print(result)