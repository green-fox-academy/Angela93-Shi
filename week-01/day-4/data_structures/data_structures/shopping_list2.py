price = {"Milk": 1.07, "Rice": 1.59, "Eggs": 3.14, "Cheese": 12.60, "Chicken Breasts": 9.40, "Apples": 2.31, "Tomato": 2.58, "Potato": 1.75, "Onion": 1.10}
Bob = {"Milk": 3, "Rice": 2, "Eggs": 2, "Cheese": 1, "Chicken Breasts": 4, "Apples": 1, "Tomato": 2, "Potato": 1 }
Alice = {"Rice": 1, "Eggs": 5, "Chicken Breasts": 2, "Apples": 1, "Tomato": 10}
# Create an application which solves the following problems.
# How much does Bob pay?
total_bob=0
for key in Bob:
    total_bob=total_bob+Bob[key]
print(total_bob)
# How much does Alice pay?
total_alice=0
for key in Alice:
    total_alice=total_alice+Alice[key]
print(total_alice)
# Who buys more Rice?
a=price["Rice"]
b=Bob["Rice"]
c=Alice["Rice"]
max_num=max(a,b,c)
if max_num == price["Rice"]:
    print("price")
elif max_num == Bob["Rice"]:
    print("Bob")
else:
    print("Alice")
# Who buys more Potato?
d=price["Potato"]
e=Bob["Potato"]
max_num2=max(d,e)
if max_num2 == price["Potato"]:
    print("price")
else:
    print("Bob")
# Who buys more different products?
len_1=len(price)
len_2=len(Bob)
len_3=len(Alice)
max_len = max(len_1,len_2,len_3)
if max_len == len(price):
    print("price")
elif max_len == len(Bob):
    print("Bob")
else:
    print("Alice")
# Who buys more products? (piece)


    
