# Reuse your Sharpie class
# Create SharpieSet class 
# it contains a list of Sharpie
# count_usable() -> sharpie is usable if it has ink in it
# remove_trash() -> removes all unusable sharpies
from sharpie import sharpie

class sharpie_set():
    def __init__(self):
        self.sharpieList = []
        self.sharpieList.append(sharpie('blue',220.0,2.0))
        self.sharpieList.append(sharpie('ink',320.0,3.0))
        self.sharpieList.append(sharpie('red',150.0,0.0))
        self.sharpieList.append(sharpie('ink',150.0,0.0))
    
    def count_usable(self,count):
        for i in range(len(self.sharpieList)):
            if "ink"  == self.sharpieList[i].color:
                count += 1
        return count
    
    def remove_trash(self):
        for i in self.sharpieList:
            if i.ink_amount == 0:
                self.sharpieList.remove(i)
        return self.sharpieList
    
sharpie_set_modal = sharpie_set()

print(sharpie_set_modal.count_usable(0))
print(sharpie_set_modal.remove_trash())
