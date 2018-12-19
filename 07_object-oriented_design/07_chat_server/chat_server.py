"""
Explain how you would design a chat server. In particular, provide details
about the various backend components, classes, and methods. What would be
the hardest problems to solve?
"""


from user import *
from chat import *


class Chat_Server():
    def __init__(self):
        self.user_list = []
        self.users = {}  # users[username] = User()
        self.chat_id = 0
        self.chat_id_list = {}  # chat_id_list[ordered_list_of_users] = chat_id
        self.chat_list = {}  # chat_list[chat_id] = Chat()

        self.group_chat_id = 0
        self.chat_invite_status = {}  # chat_invite_status[] = ???


    def add_user(self, username):
        user = User(username)
        self.user_list.append(username)
        self.users[username] = user


    def get_user(self, username):
        # Example use: when client connects to the server.
        if username in self.user_list:
            return self.users[username]
        else:
            return None


    def list_people_in_chat(self, chat_id):
        current_chat = self.chat_list[chat_id]
        return current_chat.list_of_participants()


# *****************************************************************************


    def send_contact_request(self, sender, recipient):
        # Sender sends the friend request to recipient.
        if sender not in self.users:
            print('Sender not found in user list.')
            return False
        if recipient not in self.users:
            print('Recipient not found in user list.')
            return False

        # Get recipient's User object and send friend request.
        recipient_user = self.users[recipient]
        recipient_user.receive_contact_request(sender)

        # Get sender's User object and update pending request.
        sender_user = self.users[sender]
        sender_user.update_pending_request(recipient)
        return True


    def accept_contact_request(self, sender, recipient):
        # Sender is the person ANSWERING the friend request.
        if sender not in self.users:
            print('Sender not found in user list.')
            return False
        if recipient not in self.users:
            print('Recipient not found in user list.')
            return False

        # Recipient is the person who SENT the friend request.
        recipient_user = self.users[recipient]
        recipient_user.confirm_contact_request(sender)

        # Sender is the person who REPLIED to the request.
        sender_user = self.users[sender]
        sender_user.confirm_contact_request(recipient)
        return True


    def deny_contact_request(self, sender, recipient):
        # Sender is the person ANSWERING the friend request.
        if sender not in self.users:
            print('Sender not found in user list.')
            return False
        if recipient not in self.users:
            print('Recipient not found in user list.')
            return False

        # Recipient is the person who SENT the friend request.
        recipient_user = self.users[recipient]
        recipient_user.deny_contact_request(sender)

        # Sender is the person who REPLIED to the request.
        sender_user = self.users[sender]
        sender_user.deny_contact_request(recipient)
        return True


# *****************************************************************************


    def get_chat_id(self, participants):
        # Look for an existing chat between these participants.
        # If previous chat log is not available, start new chat log.
        if participants not in self.chat_id_list:
            chat_id = self.chat_id
            self.chat_id += 1

            self.chat_id_list[participants] = chat_id
            new_chat = Chat(self, participants, chat_id)  # ???
            self.chat_list[chat_id] = new_chat

        # Otherwise, resume the chat log.
        else:
            chat_id = self.chat_id_list[participants]

        return chat_id


    def send_message(self, chat_id, sender, message):
        active_chat = self.chat_list[chat_id]
        active_chat.send_message(sender, message)


    def invite_to_group_chat(self, chat_id, sender, invited_user):
        invited = self.users[invited_user]
        invited.update_group_chat_request((sender, chat_id))

        # if user accepts, then new function return new chat id


    def accept_chat_invite(self, chat_id, accepted_user):
        # this is the chat_id of the chat with the old list of participants
        old_chat = self.chat_list[chat_id]
        previous_group = old_chat.list_of_participants()
        new_group = previous_group[:]
        new_group.append(accepted_user)

        new_chat_id = get_chat_id(new_group)

        # clean up user's group chat requests
        return new_chat_id


    def check_invite_status(self, chat_id, invited_user):
        return None







