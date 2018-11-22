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


user_1.send_contact_request('user_2')
user_2.check_contact_requests()
user_1.send_contact_request('user_3')
user_2.send_contact_request('user_3')
user_3.check_contact_requests()


# Test chat
user_1.chat('user_2', 'hello user_2!')


