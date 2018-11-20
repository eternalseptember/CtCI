# Chat object for conversations.


from datetime import datetime


class Chat():
    def __init__(self, participants, chat_id):
        # Participants should be a list of users in the chat.
        self.participants = participants
        self.chat_id = chat_id  # should be set by the server to find chat logs
        self.chat_log = self.start_chat_log()
        # location of chat logs?


    def invite_to_chat(self, participant):
        # If the user accepts the chat invitation:
        self.participants.append(participant)


    def start_chat_log(self):
        # Pretend that the chat log is like the chat window.

        # placeholder - should return file address
        file_name = 'chat_logs/' + str(self.chat_id) + '.txt'
        chat_log = open(file_name, 'w')
        chat_log.write('write to chat log: {0}'.format(file_name))
        # close file stream?
        return file_name


    def send_message(self, sender, message):
        chat_log = open(str(self.chat_log), 'a')
        time_sent = datetime.now().strftime('%b %d, %Y %I:%M:%S')
        sent_by = str(sender)
        chat_log.write('{0} {1}: {2}'.format(time_sent, sent_by, message))


    def __str__(self):
        chat_summary = ''

        for participant in self.participants:
            if len(chat_summary) > 0:
                chat_summary += ', '
            chat_summary += str(participant)

        return chat_summary



