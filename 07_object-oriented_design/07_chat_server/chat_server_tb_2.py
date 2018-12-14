# Testing simple chat and group chat.

from chat_server import *


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


# CHECKING THAT USERS ARE IN EACH OTHER'S CONTACT LISTS
# NOT YET IMPLEMENTED


# Chat, method 1
chat_1_id = user_1.chat(['user_2'], 'hey what\'s up?')
user_2.chat(['user_1'], 'doing well, you?')

# Chat, method 2
chat_1 = ['user_2', 'user_1']
user_1.chat(chat_1, 'there\'s a meeting on tuesday')
user_2.chat(chat_1, 'there is?')


# Inviting others to chat
chat_2_id = None
# chat_id = user_2.chat(['user_1'], 'going to invite someone else to this chat')
# user_2.invite_to_chat(chat_id, 'user_3')

# once the invitation has been accepted, assign it to chat_2_id


# test group chat and private chat at the same time
# pretend that chat_ids are selected based on the active window



