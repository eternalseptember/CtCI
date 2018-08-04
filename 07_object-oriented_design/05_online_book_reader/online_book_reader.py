# Design the data structures for an online book reader system.


class Book():
    def __init__(self, id, title, author, year, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def __str__(self):
        desc = str(self.title)
        return desc


class Entry():
    def __init__(self, book):
        self.book = book
        self.date_added = None  # should automatically fill this
        self.last_accessed = None
        self.favorites = False
        self.last_page_read = None  # page number when last_accessed has a value
        self.bookmarked_pages = []



class Library():
    def __init__(self):
        books = None


    def add_book(self, book):
        books.append(book)

        # when a book is added, use the entry object instead



