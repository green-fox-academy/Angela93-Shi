map={'Eggs':200,'Milk':200,'Fish':400,'Apples':150,'Bread':50,'Chicken':550}
# Create an application which solves the following problems. 
# Which products cost less than 201? (just the name)
# Which products cost more than 150? (name + price)

for key,values in map.items():
    if map[key]<201:
        print(map[key])

for key,values in map.items():
    if map[key]>150:
        print(map[key])