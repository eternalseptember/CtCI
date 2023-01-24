# Testing the simple functions.

from chat_server import *


def print_users():
	# User profile information.
	user_1.print_user_summary()
	user_2.print_user_summary()
	user_3.print_user_summary()


# Begin test.
chat_server = Chat_Server()


# Create users on the server.
chat_server.add_user('user_1')
chat_server.add_user('user_2')
chat_server.add_user('user_3')


# Logging in from client interface.
user_1 = chat_server.get_user('user_1')
user_1.login(chat_server)
user_2 = chat_server.get_user('user_2')
user_2.login(chat_server)
user_3 = chat_server.get_user('user_3')
user_3.login(chat_server)


# Activities from client interface.
user_1.update_status('online')


# Check that someone is in a user's contact list before starting chat.
# There should be an error message.
user_1.chat(['user_2'], 'we are not friends yet')
user_2.chat(['user_1'], 'no, we\'re not')


# Checking and adding people to contacts list.
user_1.send_contact_request('user_4')  # Not a valid user.
user_1.send_contact_request('user_2')
user_2.send_contact_request('user_3')
user_1.send_contact_request('user_3')
user_2.check_contact_requests()
user_3.check_contact_requests()


"""
# Manually adding contacts here.
user_1.confirm_contact_request('user_2')
user_2.confirm_contact_request('user_1')
"""

print_users()


# Chat, method 1: only passing in the list the sender is talking to.
user_1.chat(['user_2'], 'good morning')
user_2.chat(['user_1'], 'good morning to you too')

# Chat, method 2: passing in full list of chat participants.
chat_1 = ['user_2', 'user_1']
user_1.chat(chat_1, 'what\'s on the schedule today?')
user_2.chat(chat_1, 'we need to meet a client at 10:30')

# Chat, method 3: passing chat id of an existing chat.
user_1.chat(0, 'which client?')
user_2.chat(0, 'cyberdyne')







