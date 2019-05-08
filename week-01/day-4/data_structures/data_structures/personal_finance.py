# We are going to represent our expenses in a list containing integers.
# Create a list with the following items. 
# 500, 1000, 1250, 175, 800 and 120
# Create an application which solves the following problems. 
list=[500,1000,1250,175,800,120]
# How much did we spend?
total=0
max_num=0
def expense(list):
    global total
    for i in range(len(list)):
        total=total+list[i]
expense(list)
print(total)

# Which was our greatest expense?

def max_num_func(list):
    global max_num
    for i in range(len(list)):
        if list[i]>max_num:
            max_num=list[i]
        else:
            return(max_num)
max_num_func(list)
print(max_num)

# Which was our cheapest spending?

def cheaper_num_func(list):
    cheaper_num=list[0]
    for i in range(len(list)):
        if list[i]<cheaper_num:
            cheaper_num=list[i]
    return cheaper_num
print(cheaper_num_func(list))
# What was the average amount of our spendings?

average_num=0
def average_func(list):
    global average_num
    global total
    for i in range(len(list)):
        total=total+list[i]
    average_num=total/len(list)
    return average_num

print(average_func(list))




