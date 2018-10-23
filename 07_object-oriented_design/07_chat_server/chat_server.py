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
        self.sent_requests.append(target_contact)  # data format?
        # send contact request through the server
        chat_server.user_contact_request(self.username, target_contact)


    def receive_contact_request(self, sender):
        self.received_requests.append(sender)


    def check_contact_requests(self, chat_server, sender):
        # return True if invite is accepted
        return False


    def __str__(self):
        return str(self.username)



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


    def user_contact_request(self, sender, recipient):
        if sender not in self.users:
            return None
        if recipient not in self.users:
            return None

        # get recipient's User object and send friend request
        recipient_object = self.users[recipient]
        recipient_object.receive_contact_request(sender)





