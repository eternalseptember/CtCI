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


class Catalog_Entry():
    def __init__(self, book):
        self.book = book  # book object
        self.readers = []  # list of user_ids of people who own the book
        self.num_of_readers = 0  # number of people who have the book
        self.favorited = 0  # number of pepole who favorited the book


    def __str__(self):
        summary = '\t{0}\n'.format(self.book)

        # format the list of user_ids who have the book
        list_of_readers = ''
        for reader in self.readers:
            # add commas if there is a list of user ID's
            if len(list_of_readers) > 0:
                list_of_readers += ', '

            list_of_readers += str(reader)
        list_of_readers += '\n'

        summary += ('\tReaders: ' + list_of_readers)

        summary += '\tNum of Readers: {0}\n'.format(self.num_of_readers)
        summary += '\tFavorited: {0}\n'.format(self.favorited)

        return summary


class User():
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        # other info, like phone number, billing, etc


    def __str__(self):
        user_info = '{0} - {1} {2}\n'\
            .format(self.user_id, self.first_name, self.last_name)

        return user_info


class User_Book_Entry():
    def __init__(self):
        self.date_added = None  # should automatically fill this
        self.last_accessed = None
        self.favorite = False
        self.last_page_read = None  # page number when last_accessed has a value
        self.bookmarked_pages = []


class User_Library():
    def __init__(self):
        self.list_of_books = {}  # each user's books


    def add_book(self, book_id):
        if book_id not in self.list_of_books:
            self.list_of_books[book_id] = User_Book_Entry()




# Service library manages everything.
class Service_Library():
    def __init__(self):
        self.book_id = 1
        self.list_of_books = {}  # list_of_books[book_id] = Catalog_Entry()

        self.user_id = 1
        self.user_libraries = {}  # user_libraries[user_id] = User_Library()


    def add_user(self, user):
        # Multiple users may have the same name.
        first_name, last_name = user
        new_user = User(self.user_id, first_name, last_name)
        self.user_libraries[self.user_id] = new_user
        self.user_id += 1


    def add_book_to_catalog(self, book):
        author, title, publisher, year = book
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.book_id] = Catalog_Entry(new_book)
        self.book_id += 1


    def add_book_to_user_library(self, user_id, book_id):
        # CHECK THIS AREA
        book_entry = self.list_of_books[book_id]
        book_entry.append(user_id)
        book_entry.num_of_readers += 1
        # UPDATE USER'S BOOK ENTRY



    def __str__(self):
        summary = ''
        for book_id in self.list_of_books.keys():
            summary += 'Book ID: {0}\n '.format(book_id)
            summary += '{0}\n'.format(self.list_of_books[book_id])

        summary += '**********************************************************\n'

        for user_id in self.user_libraries.keys():
            summary += '{0}\n'.format(self.user_libraries[user_id])

        return summary













