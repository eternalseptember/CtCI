"""
Explain how you would design a chat server. In particular, provide details
about the various backend components, classes, and methods. What would be
the hardest problems to solve?
"""


class User():
    def __init__(self, username):
        self.username = username
        self.contacts = []
        self.status_message = ''


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
        self.users = []  # username and status?
        self.log = ''


    def add_user(self, username):
        self.users.append(username)



