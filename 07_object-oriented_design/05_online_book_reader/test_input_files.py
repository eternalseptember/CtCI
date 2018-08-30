# Making sure the text files are read and processed correctly.


import csv


with open("books.txt", "r") as books_list:

    books_info = csv.reader(books_list, skipinitialspace=True, quotechar='"')

    for book in books_info:
        print('Author: {0}'.format(book[0]))
        print('Title: {0}'.format(book[1]))
        print('Publisher: {0}'.format(book[2]))
        print('Year: {0}'.format(book[3]))
        print()
