from online_book_reader import *
from test_books import *
from test_users import *
from test_add_book import *
from test_reading import *
from test_favorites import *


service_library = Service_Library()


# Add Books to Library.
books_to_add = [hp1, hp2, hp3, lotr, asoiaf1, asoiaf2, asoiaf3]

for book in books_to_add:
    service_library.add_book_to_catalog(book)


# Add users.
users_to_add = [user01, user02, user03, user04, user05,
                user06, user07, user08, user09, user10,
                user11, user12, user13, user14, user15]

for user in users_to_add:
    service_library.add_user(user)


# Users adding books to their own library.
ownership_list = [ownership_pair_01, ownership_pair_02, ownership_pair_03,
                  ownership_pair_04, ownership_pair_05, ownership_pair_06,
                  ownership_pair_07, ownership_pair_08, ownership_pair_09,
                  ownership_pair_10]

for user_book_pair in ownership_list:
    service_library.add_book_to_user_library(user_book_pair)

print(service_library)

# Users reading the book.


# Users bookmarking pages within the book.


# Users favoriting the book.




