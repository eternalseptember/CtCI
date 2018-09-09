# Testing the online book reader system.


from online_book_reader_system import *
import csv


csv.register_dialect(
    'custom',
    skipinitialspace=True,
    quotechar='"'
    )


service_library = Service_Library()


# Add books to system library.
with open("books.txt", "r") as books_list:
    books_info = csv.DictReader(books_list, dialect='custom')

    for book in books_info:
        author = book['Author']
        title = book['Title']
        publisher = book['Publisher']
        year = int(book['Year'])

        service_library.add_book_to_catalog(author, title, publisher, year)


# Add users.
with open("users.txt", "r") as users_list:
    users_info = csv.DictReader(users_list, dialect='custom')

    for user in users_info:
        user_name = user['user_name']
        first_name = user['first_name']
        last_name = user['last_name']

        service_library.add_user(user_name, first_name, last_name)


# Users adding books to their own library.
with open("users_books.txt", "r") as ownership_list:
    ownership_info = csv.DictReader(ownership_list, dialect='custom')

    for ownership in ownership_info:
        user_id = int(ownership['user_id'])
        book_id = int(ownership['book_id'])
        date_added = ownership['date_added']

        service_library.add_book_to_user_library(user_id, book_id, date_added)


# Users reading the book.
with open("users_read.txt", "r") as reading_list:
    activity_info = csv.DictReader(reading_list, dialect='custom')

    for activity in activity_info:
        user_id = int(activity['user_id'])
        book_id = int(activity['book_id'])
        last_page = int(activity['last_page'])
        date_accessed = activity['date_accessed']

        service_library.user_reads_book(user_id, book_id, last_page, date_accessed)


# Users bookmarking pages within the book.
with open("users_bookmarks.txt", "r") as bookmark_list:
    bookmark_info = csv.DictReader(bookmark_list, dialect='custom')

    for activity in bookmark_info:
        user_id = int(activity['user_id'])
        book_id = int(activity['book_id'])
        page_num = int(activity['page_num'])

        service_library.user_bookmarks_page(user_id, book_id, page_num)


# Users favoriting the book.
with open("users_favorites.txt", "r") as favorites_list:
    favorites_info = csv.DictReader(favorites_list, dialect='custom')

    for favorite in favorites_info:
        user_id = int(favorite['user_id'])
        book_id = int(favorite['book_id'])

        service_library.user_favorites_book(user_id, book_id)



service_library.print_books_info()
service_library.print_users_info()




