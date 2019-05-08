#Create a list ('List A') which contains the following values 
#Apple, Avocado, Blueberries, Durian, Lychee
list_A=['Apple','Avocado','Blueberries','Durian','Lychee']
#Create a new list ('List B') with the values of List A
list_B=['Apple','Avocado','Blueberries','Durian','Lychee']
print(list_A)
print(list_B)
#Print out whether List A contains Durian or not
print('Durian' in list_A)
#Remove Durian from List B
list_B.remove('Durian')
print(list_A)
print(list_B)
#Add Kiwifruit to List A after the 4th element
list_A.insert(4,'kiwifruit')
print(list_A)
#Compare the size of List A and List B
if len(list_A) > len(list_B):
    print("List_A has more values")
else:
     print("List_B has more values")
#Get the index of Avocado from List A
print(list_A.index("Avocado"))
#Get the index of Durian from List B
print(list_B.index("Blueberries"))
#Add Passion Fruit and Pummelo to List B in a single statement
list_B.extend(["Passion Fruit","Pummelo"])
print(list_B)
#Print out the 3rd element from List A
print(list_A[2])