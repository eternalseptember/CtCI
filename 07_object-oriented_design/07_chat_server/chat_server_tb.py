from chat_server import *


chat_server = Chat_Server()

# Create users on the server.
chat_server.add_user('test_user_1')
chat_server.add_user('test_user_2')
chat_server.add_user('test_user_3')

# Logging in from client interface.
user_1 = chat_server.get_user('test_user_1')
user_2 = chat_server.get_user('test_user_2')
user_3 = chat_server.get_user('test_user_3')

# Activity from client interface.
user_1.send_contact_request(chat_server, 'test_user_2')


# User profile information.
print(user_1)
print(user_2)
print(user_3)


