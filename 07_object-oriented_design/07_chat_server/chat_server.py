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


    def begin_chat(self, participants):
        # Look for an existing chat between these participants.
        participants.sort()
        participants = tuple(participants)

        # If previous chat log is not available, start new chat log.
        if participants not in self.chat_id_list:
            chat_id = self.chat_id
            self.chat_id += 1

            self.chat_id_list[participants] = chat_id
            new_chat = Chat(participants, chat_id)
            self.chat_list[chat_id] = new_chat

        # Otherwise, resume the chat log.
        else:
            chat_id = self.chat_id_list[participants]

        return chat_id


    def chat(self, chat_id, sender, message):
        active_chat = self.chat_list[chat_id]
        active_chat.send_message(sender, message)



