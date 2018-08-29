# Design the data structures for an online book reader system.


from datetime import *


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

        summary += ('\tIDs of Readers: ' + list_of_readers)
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
    def __init__(self, date_added):
        self.date_added = date_added  # should automatically fill this
        self.last_accessed = None
        self.last_page_read = None  # page number when last_accessed has a value
        self.favorite = False
        self.bookmarked_pages = []


class User_Library():
    def __init__(self):
        self.list_of_books = []
        self.user_book_info = {}  # user_book_info[book_id] = User_Book_Entry()


    def add_book(self, book_id):
        if book_id not in self.list_of_books:
            self.list_of_books.append(book_id)
            date_added = str(datetime.now())
            self.user_book_info[book_id] = User_Book_Entry(date_added)


    def read_book(self, book_id, date_accessed, last_page):
        if book_id in self.list_of_books:
            user_book_entry = self.user_book_info[book_id]
            user_book_entry.last_accessed = date_accessed
            user_book_entry.last_page_read = last_page


    def __str__(self):
        book_list = ''

        # printing book_id for now
        for book in self.list_of_books:
            # add commmas if there are more than one book
            if len(book_list) > 0:
                book_list += ', '

            book_list += '{0}'.format(book)
        book_list += '\n'

        book_str = '\tBooks Owned: ' + book_list
        return book_str




# Service library manages everything.
class Service_Library():
    def __init__(self):
        self.book_id = 1
        self.list_of_books = {}  # list_of_books[book_id] = Catalog_Entry()

        self.user_id = 1
        self.list_of_users = {}  # list_of_users[user_id] = User()
        self.user_libraries = {}  # user_libraries[user_id] = User_Library()


    def add_user(self, user):
        # Multiple users may have the same name.
        first_name, last_name = user
        new_user = User(self.user_id, first_name, last_name)
        self.list_of_users[self.user_id] = new_user
        self.user_libraries[self.user_id] = User_Library()
        self.user_id += 1


    def add_book_to_catalog(self, book):
        author, title, publisher, year = book
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.book_id] = Catalog_Entry(new_book)
        self.book_id += 1


    def add_book_to_user_library(self, user_book_pair):
        user_id, book_id = user_book_pair

        # Update book's catalog entry with new reader.
        book_entry = self.list_of_books[book_id]
        book_entry.readers.append(user_id)
        book_entry.num_of_readers += 1

        # Update user's library with new book.
        user_library = self.user_libraries[user_id]
        user_library.add_book(book_id)


    def user_read_book(self, read_book_info):
        user_id, book_id, last_page = read_book_info

        # Update the user's book info.
        user_library = self.user_libraries[user_id]
        date_accessed = str(datetime.now())
        user_library.read_book(book_id, date_accessed, last_page)

    
    def user_bookmark_page(self, bookmark_info):
        user_id, book_id, page_info = bookmark_info

        # update bookmarked pages



    def user_favorite_book(self, favorite_info):
        user_id, book_id = favorite_info

        # check if user owns the book first?

        # update book's catalog.favorites

        # update user info

        return None



    def __str__(self):
        summary = ''
        for book_id in self.list_of_books.keys():
            summary += 'Book ID: {0}\n '.format(book_id)
            summary += '{0}\n'.format(self.list_of_books[book_id])

        summary += '**********************************************************\n'

        for user_id in self.list_of_users.keys():
            summary += '{0}'.format(self.list_of_users[user_id])
            summary += '{0}\n'.format(self.user_libraries[user_id])

        return summary













