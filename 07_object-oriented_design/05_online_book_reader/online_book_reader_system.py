# Design the data structures for an online book reader system.
# Service library manages everything.

from online_book_reader_objects import *


class Service_Library():
    def __init__(self):
        self.book_id = 1
        self.list_of_books = {}  # list_of_books[book_id] = Catalog_Entry()

        self.user_id = 1
        self.list_of_users = {}  # list_of_users[user_id] = User()
        self.user_libraries = {}  # user_libraries[user_id] = User_Library()


    def add_book_to_catalog(self, author, title, publisher, year):
        new_book = Book(author, title, publisher, year)
        self.list_of_books[self.book_id] = Catalog_Entry(new_book)
        self.book_id += 1


    def add_user(self, first_name, last_name):
        # Multiple users may have the same name.
        new_user = User(self.user_id, first_name, last_name)
        self.list_of_users[self.user_id] = new_user
        self.user_libraries[self.user_id] = User_Library()
        self.user_id += 1


    def add_book_to_user_library(self, user_id, book_id, date_added):
        # Update book's catalog entry with new reader.
        book_entry = self.list_of_books[book_id]
        book_entry.readers.append(user_id)
        book_entry.num_of_readers += 1

        # Update user's library with new book.
        user_library = self.user_libraries[user_id]
        user_library.add_book(book_id, date_added)


    def user_read_book(self, user_id, book_id, last_page, date_accessed):
        # Update the user's book info.
        user_library = self.user_libraries[user_id]
        user_library.read_book(book_id, date_accessed, last_page)


    def user_bookmark_page(self, user_id, book_id, page_info):
        # update bookmarked pages

        return None


    def user_favorite_book(self, user_id, book_id):
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













