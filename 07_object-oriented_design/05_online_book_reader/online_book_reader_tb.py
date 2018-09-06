# Testing the online book reader system.


from online_book_reader_system import *
import csv


service_library = Service_Library()


# Add books to system library.
with open("books.txt", "r") as books_list:
    books_info = csv.reader(books_list, skipinitialspace=True, quotechar='"')

    for book in books_info:
        author = book[0]
        title = book[1]
        publisher = book[2]
        year = int(book[3])

        service_library.add_book_to_catalog(author, title, publisher, year)


# Add users.
with open("users.txt", "r") as users_list:
    users_info = csv.reader(users_list, skipinitialspace=True, quotechar='"')

    for user in users_info:
        user_name = user[0]
        first_name = user[1]
        last_name = user[2]

        service_library.add_user(user_name, first_name, last_name)


# Users adding books to their own library.
with open("users_books.txt", "r") as ownership_list:
    ownership_info = csv.reader(ownership_list, skipinitialspace=True, quotechar='"')

    for ownership in ownership_info:
        user_id = int(ownership[0])
        book_id = int(ownership[1])
        date_added = ownership[2]

        service_library.add_book_to_user_library(user_id, book_id, date_added)


# Users reading the book.


# Users bookmarking pages within the book.


# Users favoriting the book.
with open("users_favorites.txt", "r") as favorites_list:
    favorites_info = csv.reader(favorites_list, skipinitialspace=True, quotechar='"')

    for favorite in favorites_info:
        user_id = int(favorite[0])
        book_id = int(favorite[1])

        service_library.user_favorite_book(user_id, book_id)



print(service_library)
service_library.print_users_info()




