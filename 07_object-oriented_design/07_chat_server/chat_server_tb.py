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


# Chat, method 1
user_1.chat(['user_2'], 'hey what\'s up?')
user_2.chat(['user_1'], 'doing well, you?')

# Chat, method 2
people_in_chat = ['user_2', 'user_1']
user_1.chat(people_in_chat, 'there\'s a meeting on tuesday')
user_2.chat(people_in_chat, 'what is it about?')



# Testing inviting others to chat
# chat_id = user_2.chat(['user_1'], 'going to invite someone else to this chat')
# user_2.invite_to_chat(chat_id, 'user_3')




