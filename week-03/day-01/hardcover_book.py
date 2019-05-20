# It should have the following fields: title, author, release year, page number and weight.
# The weight must be calculated from the number of pages (every page weighs 10 grams) plus the weight of the cover which is 100 grams.
# It must have a method that returns a string which contains the following information about the book: author, title and year.
from book import Book
class Hardcover_book(Book):
    def __init__(self,author,title,release_year,page_number):
        Book.__init__(self,author,title,release_year)
        self.page_number = page_number
        self.weight = self.get_weight()
    def toString(self):
        return f'author: {self.author}, title: {self.title}, year: {self.release_year}'

    def get_weight(self):
        weight = self.page_number * 10 + 100 *2
        return weight

# Hardcover_book=Hardcover_book('Douglas Adams','The Hitchhiker\'s Guide to the Galaxy','1979',200)