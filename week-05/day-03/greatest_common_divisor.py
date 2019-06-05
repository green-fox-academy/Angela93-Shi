# Find the greatest common divisor of two numbers using recursion.
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

a= int(input("Enter the first num:"))
b = int(input("Enter the second num:"))
GCD = gcd(a,b)
print(f"the greatest common divisor between {a} and {b} is {GCD}")