# Create a generator which will always yield the next Fibonacci number.
def Fibonacci_Yield(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci(n):
    # return list(Fibonacci_Yield(n))
    f = Fibonacci_Yield(n)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))


Fibonacci(10)
