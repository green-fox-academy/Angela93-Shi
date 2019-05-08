#Create a map where the keys are strings and the values are strings with the following initial values
map={'978-1-60309-452-8':'A Letter to Jo','978-1-60309-452-7':'Lupus','978-1-60309-452-3':'Red Panda and Moon Bear','978-1-60309-461-0':'The Lab'}
print(map)
#Print all the key-value pairs in the following format
for i in range(1):
    for key in map:
        print(f"{map[key]} (ISBN {key})")
#Remove the key-value pair with key 978-1-60309-444-3
del map['978-1-60309-452-3']
print(map)
#Remove the key-value pair with value The Lab
for i in range(1):
    # for key in map:
        if map[key] == "The Lab":
            del map[key]
print(map)
#Add the following key-value pairs to the map
map.update({'978-1-60309-450-4':'They Called Us Enemy','978-1-60309-453-5':'Why Did We Trust Him?'})
print(map)
#Print whether there is an associated value with key 478-0-61159-424-8 or not
if map['978-1-60309-452-8'] in map.values():
    print(True)
else:
    print(False)

#Print the value associated with key 978-1-60309-453-5
print(map['978-1-60309-453-5'])
