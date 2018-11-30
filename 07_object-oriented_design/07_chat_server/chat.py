# Chat object for conversations.


from datetime import datetime


class Chat():
    def __init__(self, participants, chat_id):
        self.participants = participants  # List of users in the chat.
        self.chat_id = chat_id  # Set by the server to find chat logs.
        self.chat_log = self.start_chat_log()  # File location of chat log.


    def start_chat_log(self):
        # Pretend that the chat log is like the chat window.
        file_name = 'chat_logs/' + str(self.chat_id) + '.txt'
        chat_log = open(file_name, 'w')
        chat_log.close()
        return file_name


    def send_message(self, sender, message):
        chat_log = open(self.chat_log, 'a')
        time_sent = datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
        sent_by = str(sender)
        chat_log.write('[{0}] {1}: {2}\n'.format(time_sent, sent_by, message))
        chat_log.close()


    def list_of_participants(self):
        return list(self.participants)



    def __str__(self):
        chat_summary = ''

        for participant in self.participants:
            if len(chat_summary) > 0:
                chat_summary += ', '
            chat_summary += str(participant)

        return chat_summary



