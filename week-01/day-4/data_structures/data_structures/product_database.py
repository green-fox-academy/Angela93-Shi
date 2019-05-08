map={'Eggs':200,'Milk':200,'Fish':400,'Apples':150,'Bread':50,'Chicken':550}
# Create an application which solves the following problems. 
# How much is the fish?
print(map['Fish'])
# What is the most expensive product?
print(max(map,key=map.get))
# What is the average price?
total=0
for key in map:
    total=total+map[key]
average=total/len(map)
print(average)
# How many products' price is below 300?
n=0
for key in map:
    if map[key] < 300:
        n+=1
print(n)
         
# Is there anything we can buy for exactly 125?
for key,value in map.items():
    if map[key] == 125:
        print("yes")
    else:
        print("No")
        break


# What is the cheapest product?
print(min(map,key=map.get))


    