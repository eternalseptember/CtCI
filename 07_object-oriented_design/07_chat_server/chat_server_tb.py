from chat_server import *


def print_users():
    # User profile information.
    print(user_1)
    print(user_2)
    print(user_3)


chat_server = Chat_Server()

# Create users on the server.
chat_server.add_user('test_user_1')
chat_server.add_user('test_user_2')
chat_server.add_user('test_user_3')

# Logging in from client interface.
user_1 = chat_server.get_user('test_user_1')
user_2 = chat_server.get_user('test_user_2')
user_3 = chat_server.get_user('test_user_3')

# Activities from client interface.
user_1.send_contact_request(chat_server, 'test_user_2')
user_2.check_contact_requests(chat_server)
user_1.send_contact_request(chat_server, 'test_user_3')
user_3.check_contact_requests(chat_server)
user_2.send_contact_request(chat_server, 'test_user_3')
user_3.check_contact_requests(chat_server)

print_users()

