# Create a function called foreach which can take an iterable and an other function. Apply the function for all the elements in the iterable.
def foreach(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def each(*args):
    # print(*args)
    return args

result = foreach(each, [1, 2, 3], range(4, 7))
print('result = ', list(result))
