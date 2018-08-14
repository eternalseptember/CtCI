from online_book_reader import *


# Books
hp1 = ('J. K. Rowling', 'Harry Potter and the Philosopher\'s Stone', 'Scholastic', 1998)
hp2 = ('J. K. Rowling', 'Harry Potter and the Chamber of Secrets', 'Scholastic', 1998)
hp3 = ('J. K. Rowling', 'Harry Potter and the Prisoner of Azkaban', 'Scholastic', 1999)
lotr = ('J. R. R. Tolkien', 'The Lord of the Rings', 'Allen & Unwin', 1954)
asoiaf1 = ('George R. R. Martin', 'A Game of Thrones', 'Bantam Books', 1996)
asoiaf2 = ('George R. R. Martin', 'A Clash of Kings', 'Bantam Books', 1998)
asoiaf3 = ('George R. R. Martin', 'A Storm of Swords', 'Bantam Books', 2000)


books_to_add = [hp1, hp2, hp3, lotr, asoiaf1, asoiaf2, asoiaf3]


service_library = Service_Library()

for book in books_to_add:
    service_library.add_book_to_catalog(book)

print(service_library)





# Testing user side

user1 = User_Library()

# when user adds book to their own library, it updates the system's library
# add book by book_id




