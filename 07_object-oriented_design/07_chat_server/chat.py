# Chat object for conversations.


class Chat():
    def __init__(self, participant):
        # Participants should be a list of users in the chat,
        # but first, assumes that it begins as a two-party chat.
        self.participants = [participant]
        # write chat log to a text file
        # location of chat logs?


    def invite_to_chat(self, participant):
        self.participants.append(participant)



