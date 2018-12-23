# Testing simple chat and group chat.

from chat_server import *


def wait_for_group_chat_acceptance(chat_1, chat_2):
    # Simulates chatting normally while waiting for someone to join.
    # chat_1 is the chat_id with the original chat participants.
    # chat_2 is the chat_id after someone accepts group chat invite.
    if chat_2 is None:
        return chat_1
    else:
        return chat_2


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
user_4 = chat_server.get_user('user_4')
user_4.login(chat_server)
user_5 = chat_server.get_user('user_5')
user_5.login(chat_server)


# CHECKING THAT USERS ARE IN EACH OTHER'S CONTACT LISTS
# NOT YET IMPLEMENTED


# Chat, method 1
chat_1_id = user_1.chat(['user_2'], 'hey what\'s up?')
user_2.chat(['user_1'], 'doing well, you?')

# Chat, method 2
chat_1 = ['user_2', 'user_1']
user_1.chat(chat_1, 'there\'s a meeting on tuesday')
user_2.chat(chat_1, 'there is?')


# Inviting one other person to chat
chat_2_invite_num = user_2.invite_to_chat(chat_id, 'user_3')


user_3.check_group_chat_invites()

# once the invitation has been accepted, assign it to chat_2_id
user_2.check_invite_status(chat_2_invite_num)


# Invite multiple people to chat


# test group chat and private chat at the same time
# pretend that chat_ids are selected based on the active window



