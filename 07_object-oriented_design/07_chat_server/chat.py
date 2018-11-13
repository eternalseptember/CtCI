# Chat object for conversations.


class Chat():
    def __init__(self, participants):
        # Participants should be a list of users in the chat.
        self.participants = participants
        self.chat_id = 0  # should be set by the server to find chat logs
        self.chat_log = self.start_chat_log()

        # write chat log to a text file
        # location of chat logs?


    def invite_to_chat(self, participant):
        # Not sure it should be here...?
        self.participants.append(participant)


    def start_chat_log(self):
        # Pretend that the chat log is like the chat window.

        # placeholder - should return file address
        file_name = str(self.chat_id) + ".txt"
        print('write to chat log: {0}'.format(file_name))

        return file_name



