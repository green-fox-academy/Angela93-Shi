# We are going to represent a shopping list in a list containing strings.
# Create a list with the following items. 
# Eggs, milk, fish, apples, bread and chicken
# Create an application which solves the following problems. 
# Do we have milk on the list?
# Do we have bananas on the list?

list=['Eggs','milk','fish','apples','bread,chicken']

FT = 'milk' in list
print(f"list has the milk in it?{FT}")

FT = 'bananas' in list
print(f"list has the bananas in it?{FT}")