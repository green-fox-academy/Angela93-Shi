# Book has an author, a title and a release year
# Book should have an toString method that returns a string in this format: 
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
class Book():
    def __init__(self,author,title,release_year):
        self.author = author
        self.title = title
        self.release_year = release_year
    
    def toString(self):
       return f'{self.author} : {self.title} ({self.release_year})'
       


# Book('Douglas Adams','The Hitchhiker\'s Guide to the Galaxy','1979')
# Book('Frank W. Brecher','American Diplomacy and the Israeli War of Independence','2013')
# Book('Janet C. Ballantyne','Fifty Years in USAID: Stories from the Front Line','2012')