# Create a generator which will always yield the next item from the fizz buzz sequence.

def generator():
	original_list=[1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
	for i in original_list:
		yield i

g2 = generator()
for _ in range(10):
	print(next(g2))