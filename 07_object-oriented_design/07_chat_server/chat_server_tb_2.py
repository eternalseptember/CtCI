# Testing simple chat and group chat.

from chat_server import *


# Begin test.
chat_server = Chat_Server()


# Create users on the server.
chat_server.add_user('user_1')
chat_server.add_user('user_2')
chat_server.add_user('user_3')
chat_server.add_user('user_4')
chat_server.add_user('user_5')


# Logging in from client interface.
user_1 = chat_server.get_user('user_1')
user_1.login(chat_server)
user_2 = chat_server.get_user('user_2')
user_2.login(chat_server)
user_3 = chat_server.get_user('user_3')
user_3.login(chat_server)
user_4 = chat_server.get_user('user_4')
user_4.login(chat_server)
user_5 = chat_server.get_user('user_5')
user_5.login(chat_server)


# CHECKING THAT USERS ARE IN EACH OTHER'S CONTACT LISTS
user_1.confirm_contact_request('user_2')
user_2.confirm_contact_request('user_1')
# ADD CONTACTS HERE


# Chat, method 1: only passing in the list the sender is talking to.
chat_1_id = user_1.chat(['user_2'], 'hey what\'s up?')
user_2.chat(['user_1'], 'doing well, you?')

# Chat, method 2: passing in full list of chat participants.
chat_1 = ['user_2', 'user_1']
user_1.chat(chat_1, 'there\'s a meeting on friday')
user_2.chat(chat_1, 'there is?')

# Chat, method 3: passing chat id of an existing chat.
user_2.chat(0, 'we just had one!')


# START GROUP CHAT


"""
Pretend that there is a chat window UI that will automatically fill in chat
info based on user's selection, like chat number and chat type.

After a group chat invitation is made, a new group chat window opens with the
active chat participants.

Users can chat in the new group chat window while waiting for responses to
group chat invites, or they can continue their conversation in the private chat
window.

If an invited user accepted the chat request, pepole would know based on the
updated participants list the chat window UI could query from the chat object.
"""

# user_3.check_group_chat_invites()

# Invite multiple people to chat


# test group chat and private chat at the same time
# pretend that chat_ids are selected based on the active window



