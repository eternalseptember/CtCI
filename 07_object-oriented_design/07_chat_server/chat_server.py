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
        self.group_chat_status = {}
        #    group_chat_status[group_chat_id] = True (open) or False (closed)
        self.group_chat_list = {}
        #    group_chat_list[group_chat_id] = Chat()
        #    No log if group chat was closed.
        self.group_chat_invites = {}
        #    group_chat_invites[group_chat_id] =
        #        invites[recipient] = [senders]


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
    def verify_users(self, sender, recipient):
        # Helper function to check that both people are valid users.
        if sender not in self.users:
            print(sender + ' is not a valid user.')
            return False
        if recipient not in self.users:
            print(recipient + ' is not a valid user.')
            return False
        return True


    def send_contact_request(self, sender, recipient):
        # Sender sends the friend request to recipient.
        if self.verify_users(sender, recipient):
            # Get recipient's User object and send friend request.
            recipient_user = self.users[recipient]
            recipient_user.receive_contact_request(sender)

            # Get sender's User object and update pending request.
            sender_user = self.users[sender]
            sender_user.update_pending_request(recipient)


    def accept_contact_request(self, sender, recipient):
        # Sender is the person ANSWERING the friend request.
        if self.verify_users(sender, recipient):
            # Recipient is the person who SENT the friend request.
            recipient_user = self.users[recipient]
            recipient_user.confirm_contact_request(sender)

            # Sender is the person who REPLIED to the request.
            sender_user = self.users[sender]
            sender_user.confirm_contact_request(recipient)


    def deny_contact_request(self, sender, recipient):
        # Sender is the person ANSWERING the friend request.
        if self.verify_users(sender, recipient):
            # Recipient is the person who SENT the friend request.
            recipient_user = self.users[recipient]
            recipient_user.deny_contact_request(sender)

            # Sender is the person who REPLIED to the request.
            sender_user = self.users[sender]
            sender_user.deny_contact_request(recipient)


# *****************************************************************************


    def send_message(self, chat_id, sender, message, is_group_chat=False):
        if is_group_chat:
            active_chat = self.group_chat_list[chat_id]
        else:
            active_chat = self.chat_list[chat_id]
        active_chat.send_message(sender, message)


    def list_users_in_chat(self, chat_id, is_group_chat):
        if is_group_chat:
            return self.group_chat_list[chat_id].list_participants()
        else:
            return self.chat_list[chat_id].list_participants()


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
        # Other participants are added as they accept the group chat invitations.
        group_chat_id = self.group_chat_id
        self.group_chat_id += 1

        group_chat = Chat(self, [started_by], group_chat_id, True)
        self.group_chat_list[group_chat_id] = group_chat
        self.group_chat_status[group_chat_id] = True

        # Use this group_id to send group_chat invites.
        return group_chat_id


# *****************************************************************************


    def invite_to_group_chat(self, group_chat_id, sender, invited_name):
        # Send the invitation.
        invited_user = self.users[invited_name]
        invited_user.invited_to_group_chat(group_chat_id, sender)

        # Update chat request log.
        if group_chat_id not in self.group_chat_invites:
            invites_list = {}
            invites_list[invited_name] = [sender]
            self.group_chat_invites[group_chat_id] = invites_list
        else:
            invites_list = self.group_chat_invites[group_chat_id]

            if invited_name in invites_list:
                # Someone has already sent an invitation.
                other_senders = invites_list[invited_name]
                other_senders.append(sender)
            else:
                # New person being invited.
                invites_list[invited_name] = [sender]


    def clean_invites_list(self, recipient, group_chat_id):
        # Recipient is the person replying to the group_chat_invite.

        # for enter_group_chat so far. also adjust for reject_group_chat.
        if group_chat_id not in self.group_chat_invites:
            # The group chat does not exist.
            return False
        else:
            # Check that the invite is legit.
            # If someone received multiple invitations to the same group chat,
            # remove all invitations.
            group_invite_list = self.group_chat_invites[group_chat_id]

            # Look to see if recipient was invited.
            if recipient in group_invite_list:
                # Clean the server's invitations list.
                del group_invite_list[recipient]
                return True
            else:
                return False


    def enter_group_chat(self, accepting_name, group_chat_id):
        # Update group chat requests log.
        # Check whether the chat invitation was legit so that
        # uninvited users can't just barge in.
        # clean_invites_list returns True if the invitation is valid.
        invited = self.clean_invites_list(accepting_name, group_chat_id)

        # Check that chat is still ongoing.
        chat_ongoing = self.group_chat_status[group_chat_id]

        if invited and chat_ongoing:
            group_chat = self.group_chat_list[group_chat_id]
            group_chat.add_participant(accepting_name)

        # Update the user's group chat requests and group chat history.
        accepting_user = self.users[accepting_name]
        accepting_user.enter_group_chat(request, chat_ongoing)


    def reject_group_chat(self, denying_name, request):
        # Update group chat requests log.
        self.clean_invites_list(denying_name, request)

        # Update the user's group chat requests.
        denying_user = self.users[denying_name]
        denying_user.reject_group_chat(request)

        return True


    def leave_group_chat(self, group_chat_id, user):
        # Invoked by the user.
        group_chat = self.group_chat_list[group_chat_id]
        group_chat.remove_participant(user)


    def close_group_chat(self, group_chat_id):
        # Invoked by the chat object when the last user leaves the chat.
        self.group_chat_status[group_chat_id] = False
        self.group_chat_list.remove(group_chat_id)









