# Create a generator which will always yield the next item from the fizz buzz sequence.

def fizz_buzz(n):
    if n % 3 ==0 and n % 5 ==0:
        yield 'fizz_buzz'
    elif n % 3 == 0:
        yield 'fizz'
    elif n % 5 == 0:
        yield 'buzz'

f=fizz_buzz(5)
print(next(f))


    