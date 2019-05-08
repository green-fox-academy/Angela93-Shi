# - Create a function called `factorio`
#   that returns it's input's factorial

num = int(input("Please input one number: "))
def factorial(num):
    factorial=1
    for i in range(1,num + 1):
        factorial = factorial*i
    print("%d 's factorial is %d" %(num,factorial))

if num < 0:
   print("抱歉，负数没有阶乘")
elif num == 0:
   print("0 的阶乘为 1")
else:
    factorial(num)
  

     