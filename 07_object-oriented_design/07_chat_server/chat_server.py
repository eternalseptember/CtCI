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
        self.log = ''  # write this to a log


class Chat_Server():
    def __init__(self):
        self.log = ''



