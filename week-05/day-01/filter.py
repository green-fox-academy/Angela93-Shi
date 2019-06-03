# Create your own filter function. It should take an iterable and an other function.
def myFilter(func,seq):
    if func is None:
        func = bool
    for item in seq:
        if func(item):
            yield item

print(list(myFilter(None,range(-2,6))))
print(list(myFilter(str.isdigit,'123abcd456')))
print(list(myFilter(lambda x:x>5,range(10))))