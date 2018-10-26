"""
Explain how you would design a chat server. In particular, provide details
about the various backend components, classes, and methods. What would be
the hardest problems to solve?
"""


class User():
    def __init__(self, username):
        self.username = username
        self.status_message = ''
        self.contacts = []
        self.sent_requests = []
        self.received_requests = []  # Requests sent by others. Accept or deny.


    def send_contact_request(self, chat_server, target_contact):
        # Send contact request through the server.
        req = chat_server.user_contact_request(str(self.username), target_contact)

        # Append to sent_requests list after chat server returns true.
        if req:
            self.sent_requests.append(target_contact)


    def receive_contact_request(self, sender):
        self.received_requests.append(sender)


    def check_contact_requests(self, chat_server, sender):
        # go through each request and accept, deny, or skip
        return False


    def __str__(self):
        summary = '{0}\n'.format(self.username)

        contacts_list = ''
        for contact in self.contacts:
            if len(contacts_list) > 0:
                contacts_list += ', '
            contacts_list += str(contact)

        sent_list = ''
        for contact in self.sent_requests:
            if len(sent_list) > 0:
                sent_list += ', '
            sent_list += str(contact)

        received_list = ''
        for contact in self.received_requests:
            if len(received_list) > 0:
                received_list += ', '
            received_list += str(contact)

        summary += 'Contacts list: '
        summary += '{0}\n'.format(contacts_list)
        summary += 'Sent list: '
        summary += '{0}\n'.format(sent_list)
        summary += 'Received list: '
        summary += '{0}\n'.format(received_list)

        return summary


class Chat():
    def __init__(self, participants):
        # group chat?
        self.participants = participants  # list of users in the chat
        # write chat log to a text file
        # location of chat logs?


    def begin_chat(self, user_1, user_2):
        # user_1 is the person starting the chat with user_2
        # open some file streams?
        print()


    def send(self, user_1, user_2, message):
        # user_1 sends the message to user_2
        # write the message to the text file
        print()



class Chat_Server():
    def __init__(self):
        self.user_list = []
        self.users = {}  # users[username] = User()
        self.log = ''


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


    def user_contact_request(self, sender, recipient):
        if sender not in self.users:
            print('Sender not found in user list.')
            return False
        if recipient not in self.users:
            print('Recipient not found in user list.')
            return False

        # Get recipient's User object and send friend request.
        recipient_user = self.users[recipient]
        recipient_user.receive_contact_request(sender)
        return True




