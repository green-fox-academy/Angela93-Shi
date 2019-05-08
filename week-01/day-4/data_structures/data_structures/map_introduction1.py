#Create an empty map where the keys are integers and the values are characters
map={}
#Print out whether the map is empty or not
print(len(map))
#Add the following key-value pairs to the map
map[97]='a'
map[98]='b'
map[99]='c'
map[65]='A'
map[66]='B'
map[67]='C'
#Print all the keys
print(map.keys())
#Print all the values
print(map.values())
#Add value D with the key 68
map[68]='D'
#Print how many key-value pairs are in the map
print(len(map))
#Print the value that is associated with key 99
print(map[99])
#Remove the key-value pair where with key 97
del map[97]
print(map)
#Print whether there is an associated value with key 100 or not
print(100 in map.keys())
#Remove all the key-value pairs
map.clear()
print(map)