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
        self.group_chat_list = {}  # group_chat_list[group_chat_id] = Chat()
        self.chat_invite_num = 0
        self.chat_invite_info = {}
        #    chat_invite_info[chat_invite_num] = (chat_id, sender, recipient)


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


    def send_message(self, chat_id, sender, message, is_group_chat=False):
        if is_group_chat:
            active_chat = self.group_chat_list[chat_id]
        else:
            active_chat = self.chat_list[chat_id]
        active_chat.send_message(sender, message)


    def list_people_in_chat(self, chat_id, is_group_chat):
        if is_group_chat:
            self.group_chat_list[chat_id].list_participants()
        else:
            current_chat = self.chat_list[chat_id].list_participants()


    def start_chat(self, participants):
        chat_id = self.chat_id
        self.chat_id += 1

        self.chat_id_list[participants] = chat_id
        new_chat = Chat(self, participants, chat_id)
        self.chat_list[chat_id] = new_chat

        return chat_id


    def get_chat_id(self, participants):
        # Used for two-party chat.
        # Can be used for group_chat, but the problem is when additional people
        # join the chat, new chat_ids will be generated.

        # Look for an existing chat between these participants.
        # If previous chat log is not available, start new chat log.
        if participants not in self.chat_id_list:
            chat_id = self.start_chat(participants)

        # Otherwise, resume the chat log.
        else:
            chat_id = self.chat_id_list[participants]

        return chat_id


    def start_group_chat(self, participants):
        # Participants is a list of current people in chat.
        # Function invoked from outside an existing chat window.

        group_chat_id = self.group_chat_id
        self.group_chat_id += 1

        group_chat = Chat(self, participants, group_chat_id, True)
        self.group_chat_list[group_chat_id] = group_chat

        # Use this group_id to send group_chat invites.
        return group_chat_id


    def get_group_chat_id(self, chat_id):
        """
        Group chats and simple chats use different numbering systems.

        If the chat_id passed in is a simple chat, then perhaps the user
        started a group chat inside the two-party chat window.

        If the chat_id of a simple chat was passed in multiple times, then
        users invited multiple people inside the simple chat window;
        or users started a new group chat after an old group chat has ended.

        If the chat_id of a group chat was passed in, then the user invited
        people inside the group chat window.
        """
        is_group_chat = False
        if chat_id is not None:
            is_group_chat = self.chat_list[chat_id].is_group_chat

        if not is_group_chat:
            group_chat_id = self.group_chat_id
            self.group_chat_id += 1


            # Get list of participants from the previous chat
            # and use it to start a group chat.
            initial_participants = self.list_people_in_chat(chat_id)


            return group_chat_id
        else:
            return chat_id


# *****************************************************************************


    def invite_to_group_chat(self, group_chat_id, sender, invited_name):
        invite_num = self.chat_invite_num
        self.chat_invite_num += 1

        invited_user = self.users[invited_name]
        invited_user.group_chat_request((invite_num, sender, group_chat_id))
        
        return chat_invite_num


    def accept_chat_invite(self, group_chat_id, accepted_name):

        # clean up user's group chat requests
        accepted_user = self.users[accepted_name]

        # add this info to user's group chat list

        # add the new user to the group chat's participant list
        group_chat = self.group_chat_list[group_chat_id]
        group_chat.add_participant(accepted_name)

        return group_chat_id









