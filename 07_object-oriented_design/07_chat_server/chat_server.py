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
        self.chat_invite_info = {}
        #    chat_invite_info[group_chat_id] = [(sender, receiver)]


# *****************************************************************************


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
            self.chat_list[chat_id].list_participants()


    def start_chat(self, participants):
        # Used for two-party chat.
        # Can be used for group_chat, but the problem is when additional people
        # join the chat, new chat_ids will be generated.

        # Look for an existing chat between these participants.
        # If previous chat log is not available, start new chat log.
        if participants not in self.chat_id_list:
            chat_id = self.chat_id
            self.chat_id += 1

            self.chat_id_list[participants] = chat_id
            new_chat = Chat(self, participants, chat_id)
            self.chat_list[chat_id] = new_chat

        # Otherwise, resume the chat log.
        else:
            chat_id = self.chat_id_list[participants]

        return chat_id


    def start_group_chat(self, started_by):
        # The person who created the group chat is the first participant.
        # Other participants are added as they accept the group chat invitation.
        group_chat_id = self.group_chat_id
        self.group_chat_id += 1

        group_chat = Chat(self, started_by, group_chat_id, True)
        self.group_chat_list[group_chat_id] = group_chat

        # Use this group_id to send group_chat invites.
        return group_chat_id


# *****************************************************************************


    def invite_to_group_chat(self, group_chat_id, sender, invited_name):
        request = (sender, group_chat_id)
        invited_user = self.users[invited_name]
        invited_user.invited_to_group_chat(request)

        # Update self.chat_invite_info.

        return chat_invite_num


    def enter_group_chat(self, request, accepted_name):
        # Update group chat requests log.
        # Check whether the chat invitation was legit so that
        # uninvited users can't just barge in.


        # Add the new user to the group chat's participant list.
        group_chat = self.group_chat_list[group_chat_id]
        group_chat.add_participant(accepted_name)

        return True


    def reject_group_chat(self, request, rejected_name):
        # Update group chat requests log.
        return None


    def leave_group_chat(self, group_chat_id, user):
        group_chat = self.group_chat_list[group_chat_id]
        group_chat.remove_participant(user)


    def close_group_chat(self, group_chat_id):
        # INSTEAD OF REMOVING, UDPATE WITH STATUS SAYING GROUP WAS CLOSED?
        self.group_chat_list.remove(group_chat_id)









