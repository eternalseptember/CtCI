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
class Catalog_Entry():
    def __init__(self, book):
        self.book = book  # book object
        self.readers = []  # list of user_ids of people who own the book
        self.num_of_readers = 0  # number of people who have the book
        self.favorited = 0  # number of pepole who favorited the book


    def __str__(self):
        summary = '\t{0}\n'.format(self.book)
        # list of user_ids of people who own the book
        summary += '\tNum of Readers: {0}\n'.format(self.num_of_readers)
        summary += '\tFavorited: {0}\n'.format(self.favorited)

        return summary


class Service_Library():
    def __init__(self):
        self.id = 1
        self.list_of_books = {}  # list_of_books[id] = Catalog_Entry()


    def add_book_to_catalog(self, book):
        author, title, publisher, year = book
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.id] = Catalog_Entry(new_book)
        self.id += 1


    def add_book_to_user_library(self, user_id, book_id):
        book_entry = self.list_of_books[book_id]
        book_entry.append(user_id)
        book_entry.num_of_readers += 1



    def __str__(self):
        summary = ''
        for book_id in self.list_of_books.keys():
            summary += 'Book ID: {0}\n '.format(book_id)
            summary += '{0}\n'.format(self.list_of_books[book_id])

        return summary






# Individual users' libraries.
class User_Entry():
    def __init__(self):
        self.date_added = None  # should automatically fill this
        self.last_accessed = None
        self.favorites = False
        self.last_page_read = None  # page number when last_accessed has a value
        self.bookmarked_pages = []


class User_Library():
    def __init__(self, user_id):
        self.user_id = user_id
        self.list_of_books = {}  # each user's books


    def add_book(self, book_id):
        if book_id not in self.list_of_books:
            self.list_of_books[book_id] = User_Entry()





