# Making sure the text files are read and processed correctly.


import csv


csv.register_dialect(
	'custom',
	skipinitialspace=True,
	quotechar='"'
	)


with open("books.txt", "r") as books_list:

	books_info = csv.DictReader(books_list, dialect='custom')

	for book in books_info:
		print('Author: {0}'.format(book['Author']))
		print('Title: {0}'.format(book['Title']))
		print('Publisher: {0}'.format(book['Publisher']))
		print('Year: {0}'.format(int(book['Year'])))
		print()


"""
with open("books.txt", "r") as books_list:

	books_info = csv.reader(books_list, dialect='custom')

	for book in books_info:
		print('Author: {0}'.format(book[0]))
		print('Title: {0}'.format(book[1]))
		print('Publisher: {0}'.format(book[2]))
		print('Year: {0}'.format(int(book[3])))
		print()
"""
