# Bookshelf has a list of books in it
# It must be able to add books to the bookshelf
# It must be able to remove books from the bookshelf
# It must have a favouriteAuthor method which must be able to return who has written the most books in the shelf
# It must have a earliestPublished method which must be able to return the earliest published book.
# It must have a latestPublished method which must be able to return the latest published book.
# It must have a toString method which give us information about the number of books, the earliest and the latest released books, and the favourite author.

from book import Book
from hardcover_book import Hardcover_book
from paperback_book import Paperback_book
import re
import operator

class Bookshelf():
    def __init__(self):
        self.bookList = []
        self.bookList2 = []
        # self.bookList.append(Book('Douglas Adams','The Hitchhiker\'s Guide to the Galaxy','1979'))
        # self.bookList.append(Book('Frank W. Brecher','American Diplomacy and the Israeli War of Independence','1878'))
        # self.bookList.append(Book('Janet C. Ballantyne','Fifty Years in USAID: Stories from the Front Line','2012'))
        
    def add_books(self,book):
        self.bookList.append(book)
        return self.bookList
    
    def add_books2(self,hardcover_book):
        self.bookList2.append(hardcover_book)
        return self.bookList2

    def remove_books(self,book):
        self.bookList.remove(book)
        return self.bookList

    def favouriteAuthor(self):
        author_list = []
        author_dic = {}
        p=re.compile(r'(.+)\s\:\s.+\s\((\d{4})\)')
        for book in bookshelf.bookList:
            m = p.match(book.toString())
            author_list.append(m.group(1))

        author_dic = {}
        for name in author_list:
            try:
                author_dic[name] += 1
            except:
                author_dic[name] = 1
        most_author=max(author_dic, key=author_dic.get)
        return most_author

    def total_books(self):
        author_list = []
        author_dic = {}
        p=re.compile(r'(.+)\s\:\s.+\s\((\d{4})\)')
        for book in bookshelf.bookList:
            m = p.match(book.toString())
            author_list.append(m.group(1))

        author_dic = {}
        for name in author_list:
            try:
                author_dic[name] += 1
            except:
                author_dic[name] = 1
        books_total = sum(author_dic.values())
        return books_total

    def earliestPublished(self):
        published_year=[]
        p=re.compile(r'.+\s\:\s.+\s\((\d{4})\)')
        for book in bookshelf.bookList:
            m = p.match(book.toString())
            published_year.append(m.group(1))
        # print(published_year)
        earliestPublished_year = min(published_year)
        # print(earliestPublished_year)
        for book in bookshelf.bookList:
            if book.release_year == earliestPublished_year:
                # print(book.title)
                return book.title
       

    def latestPublished(self):
        published_year=[]
        p=re.compile(r'.+\s\:\s.+\s\((\d{4})\)')
        for book in bookshelf.bookList:
            m = p.match(book.toString())
            published_year.append(m.group(1))
        # print(published_year)
        latestPublished_year = max(published_year)
        # print(latestPublished_year)  
        for book in bookshelf.bookList:
            if book.release_year == latestPublished_year:
                # print(book.title)
                return book.title
       
    def get_lightest_book(self):
        booklist_dic={}
        for book in self.bookList2:
            booklist_dic[book.author] = book.page_number
        lightest_book= min(booklist_dic.values())
        for book in bookshelf.bookList2:
            if book.page_number == lightest_book:
                # print(book.title)
                return book.title
    
    def get_most_pages_book(self):
        booklist_dic={}
        for book in self.bookList2:
            booklist_dic[book.author] = book.page_number
        most_pages= max(booklist_dic.values())
        for book in bookshelf.bookList2:
            if book.page_number == most_pages:
                # print(book.title)
                return book.author

    def toString(self,books_total,earliest_book,latest_book,favourite_author,lightest_book,most_pages_author):
        return f'the number of books:{books_total},the earlist book is {earliest_book},the latest_book is {latest_book},the favourite author is {favourite_author},the lightest_book is {lightest_book},{most_pages_author} wrote the most pages'


book = Book('Douglas Adams','The Hitchhiker\'s Guide to the Galaxy','1979')

hardcover_book = Hardcover_book('Douglas Adams','The Hitchhiker\'s Guide to the Galaxy','1979',500)

bookshelf = Bookshelf()

bookshelf.add_books(book)

bookshelf.add_books2(hardcover_book)

# bookshelf.favouriteAuthor()
# bookshelf.earliestPublished()
# bookshelf.latestPublished()

books_total = bookshelf.total_books()
earliest_book = bookshelf.earliestPublished()
latest_book = bookshelf.latestPublished()
favourite_author = bookshelf.favouriteAuthor()
lightest_book = bookshelf.get_lightest_book()
most_pages_author = bookshelf.get_most_pages_book()

print(bookshelf.toString(books_total,earliest_book,latest_book,favourite_author,lightest_book,most_pages_author))
