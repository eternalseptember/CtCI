# Design the data structures for an online book reader system.


class Book():
    def __init__(self, id, title, author, year, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher


class Library():
    def __init__(self):
        books = None


    def add_book(self, book):
        books.append(book)


"""
library should keep track of
- when the book was added
- when the book was last accessed
- last page read
- favorites
- bookmarked pages
"""



