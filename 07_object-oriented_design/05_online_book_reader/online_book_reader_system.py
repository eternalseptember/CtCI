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

		# Used to check for duplicate usernames;
		# would be replaced by a normal database query.
		self.taken_usernames = []


	def add_book_to_catalog(self, author, title, publisher, year):
		new_book = Book(author, title, publisher, year)
		self.list_of_books[self.book_id] = Catalog_Entry(new_book)
		self.book_id += 1


	def add_user(self, user_name, first_name, last_name):
		if user_name not in self.taken_usernames:
			new_user = User(self.user_id, user_name, first_name, last_name)
			self.list_of_users[self.user_id] = new_user
			self.user_libraries[self.user_id] = User_Library()
			self.taken_usernames.append(user_name)
			self.user_id += 1


	def add_book_to_user_library(self, user_id, book_id, date_added):
		# Checks whether user_id and book_id are valid.
		if (user_id < 1) or (user_id >= self.user_id):
			return None
		if (book_id < 1) or (book_id >= self.book_id):
			return None

		# Update book's catalog entry with new reader.
		book_entry = self.list_of_books[book_id]
		book_entry.readers.append(user_id)

		# Update user's library with new book.
		user_library = self.user_libraries[user_id]
		user_library.add_book(book_id, date_added)


	def user_reads_book(self, user_id, book_id, last_page, date_accessed):
		# Update user's book progress.
		user_library = self.user_libraries[user_id]
		user_library.read_book(book_id, date_accessed, last_page)


	def user_bookmarks_page(self, user_id, book_id, page_num):
		# Toggle user's bookmarked pages.
		user_library = self.user_libraries[user_id]
		user_library.bookmark_page(book_id, page_num)


	def user_favorites_book(self, user_id, book_id):
		# Check user library and toggle favorites.
		user_library = self.user_libraries[user_id]
		favorite = user_library.favorite_book(book_id)

		# Update the book's catalog entry.
		if favorite is not None:
			book_entry = self.list_of_books[book_id]
			if favorite:
				book_entry.favorites.append(user_id)
			else:
				book_entry.favorites.remove(user_id)


	def print_books_info(self):
		# Print system's catalog entry for each book.
		summary = ''

		for book_id in self.list_of_books.keys():
			# Set up the information to be printed.
			book_entry = self.list_of_books[book_id]
			book_info = str(book_entry.book)
			readers = book_entry.readers  # list of user_ids
			num_of_readers = len(readers)
			favorites = book_entry.favorites  # list of user_ids
			num_of_favorites = len(favorites)

			# Format the output.
			summary += '{0}\n'.format(book_info)
			summary += '\tBook ID: {0}\n'.format(book_id)
			summary += '\tReaders: {0}\n'.format(num_of_readers)

			# Format the usernames of readers.
			list_of_readers = ''
			for user_id in readers:
				# Add commas if there is a list of user ID's.
				if len(list_of_readers) > 0:
					list_of_readers += ', '

				reader_username = self.list_of_users[user_id]
				list_of_readers += str(reader_username)


			summary += '\t\t{0}\n'.format(list_of_readers)
			summary += '\tFavorites: {0}\n'.format(num_of_favorites)

			# Format the usernames who favorited the book.
			list_of_favorited_users = ''
			for user_id in favorites:
				# Add commas if there is a list of user ID's.
				if len(list_of_favorited_users) > 0:
					list_of_favorited_users += ', '

				reader_username = self.list_of_users[user_id]
				list_of_favorited_users += str(reader_username)


			summary += '\t\t{0}\n'.format(list_of_favorited_users)
			summary += '\n'

		print(summary)


	def print_users_info(self):
		# Print information about each user's library.
		summary = ''

		for user_id in self.list_of_users.keys():
			# Get info about user and user's library.
			user_entry = self.list_of_users[user_id]
			user_library = self.user_libraries[user_id]
			list_of_books = user_library.list_of_books

			# Print the username.
			summary += '{0}: \n'.format(user_entry)

			# Format output for each book in the user's library.
			for book_id in list_of_books:
				book_entry = str(self.list_of_books[book_id].book)
				user_book_entry = user_library.user_book_info[book_id]
				date_added = user_book_entry.date_added
				date_last_accessed = user_book_entry.last_accessed
				last_page_read = user_book_entry.last_page_read
				favorite = user_book_entry.favorite
				bookmarked_pages = str(user_book_entry.bookmarked_pages)

				if favorite:
					summary += '\t* {0} *\n'.format(book_entry)
				else:
					summary += '\t{0}\n'.format(book_entry)

				summary += '\t\tAdded: {0}\n'.format(date_added)
				summary += '\t\tLast Read: {0}\n'.format(date_last_accessed)
				summary += '\t\tLast Page Read: {0}\n'.format(last_page_read)
				summary += '\t\tPages Bookmarked: {0}\n'.format(bookmarked_pages)
				summary += '\n'

		print(summary)






