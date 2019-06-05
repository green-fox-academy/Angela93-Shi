# Given a non-negative integer n, return the sum of its digits recursively (without loops).

def sum_digit(n):
    if n==0:
        return 0
    else:
        return n % 10 + sum_digit(n // 10)

print(sum_digit(126))