Oliver = {"Laptop", "Notebook", "Pen", "Sunglasses", "Hand sanitizer"}
Ethen = {"Sunglasses", "Notebook", "Phone"}
Mia = {"Laptop", "Sunglasses", "Hand sanitizer"}

# Write an application that answers the following questions
# What are the common items in Oliver's and Ethan's bag?
print(Oliver&Ethen)
# What are the items that in Oliver's bag but not in Mia's bag?
print(Oliver^Mia)
# What are the common items in Oliver's, Ethan's and Mia's bag?
print(Oliver&Ethen&Mia)