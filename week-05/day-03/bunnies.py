# We have a number of bunnies and each bunny has two big floppy ears. 
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunnies_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + bunnies_ears(n-1)

n = int(input("Enter the number of bunnies: "))
number_of_ears = bunnies_ears(n)
print(f'{n} bunnies have {number_of_ears} ears')
