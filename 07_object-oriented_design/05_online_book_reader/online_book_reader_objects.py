# Design the data structures for an online book reader system.
# Basic objects used by the system for managing the library.


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
        self.num_of_readers = 0  # number of people who have the book
        self.readers = []  # user_ids of owners
        self.num_of_favorites = 0  # number of people who favorited the book
        self.favorites = []  # user_ids of favoriting users


    def __str__(self):
        summary = '{0}\n'.format(self.book)
        summary += 'Num of Readers: {0}\n'.format(self.num_of_readers)

        # Format the list of user_ids of owners.
        list_of_readers = ''
        for reader in self.readers:
            # Add commas if there is a list of user ID's.
            if len(list_of_readers) > 0:
                list_of_readers += ', '

            list_of_readers += str(reader)
        list_of_readers += '\n'

        summary += ('IDs of Readers: ' + list_of_readers)
        summary += 'Num of Favorited: {0}\n'.format(self.num_of_favorites)

        # Format the list user_ids who favorited the book.
        list_of_favorited_users = ''
        for reader in self.favorites:
            # Add commas if there is a list of user ID's.
            if len(list_of_favorited_users) > 0:
                list_of_favorited_users += ', '

            list_of_favorited_users += str(reader)
        list_of_favorited_users += '\n'

        summary += ('Who favorited: ' + list_of_favorited_users)
        return summary


class User():
    def __init__(self, user_id, user_name, first_name, last_name):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        # other info, like phone number, billing, etc

    def __str__(self):
        return str(self.user_name)


class User_Book_Entry():
    def __init__(self, date_added):
        self.date_added = date_added
        self.last_accessed = None
        self.last_page_read = None  # page number when last_accessed has a value
        self.favorite = False
        self.bookmarked_pages = []


class User_Library():
    def __init__(self):
        self.list_of_books = []  # book_id
        self.list_of_favorites = []  # book_id
        self.user_book_info = {}  # user_book_info[book_id] = User_Book_Entry()


    def add_book(self, book_id, date_added):
        if book_id not in self.list_of_books:
            self.list_of_books.append(book_id)
            self.user_book_info[book_id] = User_Book_Entry(date_added)


    def read_book(self, book_id, date_accessed, last_page):
        if book_id in self.list_of_books:
            user_book_entry = self.user_book_info[book_id]
            user_book_entry.last_accessed = date_accessed
            user_book_entry.last_page_read = last_page


    def bookmark_page(self, book_id, page_num):
        if book_id not in self.list_of_books:
            return None

        else:
            book = self.user_book_info[book_id]

            # Toggle bookmarked page.
            if page_num in book.bookmarked_pages:
                book.bookmarked_pages.remove(page_num)
            else:
                book.bookmarked_pages.append(page_num)
                book.bookmarked_pages.sort()


    def favorite_book(self, book_id):
        if book_id not in self.list_of_books:
            return None

        else:
            book = self.user_book_info[book_id]

            # Toggle favorites
            if book.favorite:
                self.list_of_favorites.remove(book_id)
                book.favorite = False
                return False
            else:
                self.list_of_favorites.append(book_id)
                book.favorite = True
                return True


    def __str__(self):
        book_list = ''

        # printing book_id for now
        for book in self.list_of_books:
            # add commmas if there are more than one book
            if len(book_list) > 0:
                book_list += ', '

            book_list += '{0}'.format(book)
        book_list += '\n'

        # book_str = '\tBooks Owned: ' + book_list
        return book_list


