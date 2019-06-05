# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. 
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. 
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunnies2(n):
    if n==0:
        return 0
    else:
        if (n % 2 == 1):
            return 2 + bunnies2(n-1)
        elif (n % 2 == 0):
            return 3 + bunnies2(n-1)

n = int(input("Enter the number of bunnies: "))
number_of_ears = bunnies2(n)
print(f'{n} bunnies have {number_of_ears} ears')