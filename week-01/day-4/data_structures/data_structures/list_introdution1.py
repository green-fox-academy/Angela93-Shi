#Create an empty list which will contain names (strings)
list=[]
#Print out the number of elements in the list
print(len(list))
#Add William to the list
list.insert(0,'William')
#Print out whether the list is empty or not
print(list)
#Add John to the list
list.insert(1,'John')
#Add Amanda to the list
list.insert(2,'Amanda')
#Print out the number of elements in the list
print(len(list))
#Print out the 3rd element
print(list[2])
#Iterate through the list and print out each name 
for i in range(len(list)):
    print(list[i])

#Iterate through the list and print 
for i in range(len(list)):
    print(f"{i+1}. {list[i]}")

#Remove the 2nd element
list.remove(list[1])
print(list)
#Iterate through the list in a reversed order and print out each name 
list.reverse()
print(list)
#Remove all elements
for i in range(len(list)):
    list.remove(list[len(list)-1])
    if len(list)==0:
        break
print(list)
