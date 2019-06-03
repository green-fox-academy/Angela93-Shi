# Create your own map function. It should take an iterable and an other function.
def map(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def add(*args):
    # print(*args)
    return sum(args)

result = map(add, [1, 2, 3], range(4, 7))
print('result = ', list(result))
