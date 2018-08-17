from online_book_reader import *
from test_books import *
from test_users import *


service_library = Service_Library()


# Add Books to Library
books_to_add = [hp1, hp2, hp3, lotr, asoiaf1, asoiaf2, asoiaf3]

for book in books_to_add:
    service_library.add_book_to_catalog(book)


# Add users
users_to_add = [user01, user02, user03, user04, user05,
                user06, user07, user08, user09, user10,
                user11, user12, user13, user14, user15,
                user16, user17, user18, user19, user20]

for user in users_to_add:
    service_library.add_user(user)


print(service_library)


# Users adding books to their own library


# Users accessing and updating the book



