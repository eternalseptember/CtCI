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
        self.list_of_books = {}  # list_of_books[id] = Book_Entry()


    def add_book(self, book):
        author, title, publisher, year = book
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.id] = Book_Entry(new_book)
        self.id += 1


    def __str__(self):
        summary = ''
        for book_id in self.list_of_books.keys():
            summary += '{0}\n'.format(self.list_of_books[book_id])

        return summary


class Book_Entry():
    def __init__(self, book):
        self.book = book  # book object
        self.readers = 0  # number of people who have the book
        self.favorited = 0  # number of pepole who favorited the book


    def __str__(self):
        summary = '{0}\n'.format(self.book)
        summary += '\tReaders: {0}\n'.format(self.readers)
        summary += '\tFavorited: {0}\n'.format(self.favorited)

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







