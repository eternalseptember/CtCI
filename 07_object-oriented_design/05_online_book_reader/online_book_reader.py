# Design the data structures for an online book reader system.


class Book():
    def __init__(self, author, title, publisher, year):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year

    def __str__(self):
        desc = '{0} - '.format(self.author)
        desc += '{0}, '.format(self.title)
        desc += '{0}, '.format(self.publisher)
        desc += '{0}'.format(self.year)
        return desc


# Library managed by the service, rather than individual users.
class Service_Library():
    def __init__(self):
        self.id = 1
        self.list_of_books = {}  # list_of_books[id] = Book()


    def add_book(self, book):
        author, title, publisher, year = book
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.id] = new_book
        self.id += 1


    def __str__(self):
        summary = ''
        for book_id in self.list_of_books.keys():
            summary += '{0}\n'.format(self.list_of_books[book_id])

        return summary




# User-specific info
class Entry():
    def __init__(self, book):
        self.book = book
        self.date_added = None  # should automatically fill this
        self.last_accessed = None
        self.favorites = False
        self.last_page_read = None  # page number when last_accessed has a value
        self.bookmarked_pages = []







