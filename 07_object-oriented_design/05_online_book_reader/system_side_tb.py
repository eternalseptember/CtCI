from online_book_reader import *
from test_books import *


service_library = Service_Library()


# Add Books to Library
books_to_add = [hp1, hp2, hp3, lotr, asoiaf1, asoiaf2, asoiaf3]

for book in books_to_add:
    service_library.add_book_to_catalog(book)

print(service_library)


# Add users
users_to_add = []


# Users adding books to their own library


# Users accessing and updating the book



