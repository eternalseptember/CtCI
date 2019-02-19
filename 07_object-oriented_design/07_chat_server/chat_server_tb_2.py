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
chat_server.add_user('user_6')


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
user_6 = chat_server.get_user('user_6')
user_6.login(chat_server)


# Contact requests is tested in tb_1.py.
# Manually adding contacts here.
user_1.confirm_contact_request('user_2')
user_2.confirm_contact_request('user_1')

user_1.confirm_contact_request('user_3')
user_3.confirm_contact_request('user_1')

user_1.confirm_contact_request('user_5')
user_5.confirm_contact_request('user_1')

user_2.confirm_contact_request('user_4')
user_4.confirm_contact_request('user_2')

user_2.confirm_contact_request('user_3')
user_3.confirm_contact_request('user_2')


# Chat, method 1: only passing in the list the sender is talking to.
chat_1_id = user_1.chat(['user_2'], 'hey what\'s up?')
user_2.chat(['user_1'], 'doing well, you?')

# Chat, method 2: passing in full list of chat participants.
chat_1 = ['user_2', 'user_1']
user_1.chat(chat_1, 'there\'s a meeting on friday')
user_2.chat(chat_1, 'there is?')

# Chat, method 3: passing chat id of an existing chat.
user_2.chat(0, 'we just had one!')

# No group chat started yet.
user_1.check_group_chat_invites()


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


# GROUP CHAT 1
print()
group_chat_1 = ['user_1', 'user_2', 'user_3']
group_chat_1_id = user_1.start_group_chat(group_chat_1)

user_1.check_group_chat_invites()  # There should be no invites.
user_2.check_group_chat_invites()
user_3.check_group_chat_invites()

# group chat and private chat at the same time
# pretend that chat_ids are selected based on the active window
user_3.chat(group_chat_1_id, 'what\'s up everyone?', True)
user_1.chat(group_chat_1_id, 'hey', True)
user_2.chat(group_chat_1_id, 'hi', True)
user_1.chat(chat_1_id, 'where\'s the food truck you went to yesterday?')
user_2.chat(chat_1_id, 'two blocks downtown')


# GROUP CHAT 2
print()
group_chat_2 = ['user_1', 'user_2', 'user_3', 'user_5']
group_chat_2_id = user_1.start_group_chat(group_chat_2)

user_2.check_group_chat_invites()
user_3.check_group_chat_invites()
user_5.check_group_chat_invites()

# inviting people to an ongoing chat
# user_2 inviting user_4 to chat
user_1.chat(group_chat_2_id, 'hey what\'s up everyone?', True)
user_2.chat(group_chat_2_id, 'I\'m inviting user_4.', True)
user_3.chat(group_chat_2_id, 'ok', True)
user_2.invite_to_group_chat(group_chat_2_id, 'user_4')

user_4.check_group_chat_invites()
user_4.chat(group_chat_2_id, 'hi', True)
user_5.chat(group_chat_2_id, 'I need to go.', True)


# test closing a group chat
user_5.leave_group_chat(group_chat_2_id)
print(chat_server.list_users_in_chat(group_chat_2_id, True))
user_4.leave_group_chat(group_chat_2_id)
print(chat_server.list_users_in_chat(group_chat_2_id, True))
user_3.leave_group_chat(group_chat_2_id)
print(chat_server.list_users_in_chat(group_chat_2_id, True))
user_2.leave_group_chat(group_chat_2_id)
print(chat_server.list_users_in_chat(group_chat_2_id, True))
user_1.leave_group_chat(group_chat_2_id)  # last person
print(chat_server.list_users_in_chat(group_chat_2_id, True))



