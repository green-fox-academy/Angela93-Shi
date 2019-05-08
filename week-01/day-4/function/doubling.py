# - Create a variable named `base_num` and assign the value `123` to it
# - Create a function called `doubling` that doubles it's input parameter and returns with an integer
# - Print the result of `doubling(base_num)`

base_num=123
def doubling(a):
    global base_num
    a =base_num*2
    return a

doubling(base_num)
print(doubling(base_num))