# Chat object for conversations.


from datetime import datetime


class Chat():
	def __init__(self, server, participants, chat_id, is_group_chat=False):
		self.chat_server = server  # Chat server managing this chat.
		self.participants = participants  # List of users in the chat.
		self.chat_id = chat_id  # Set by the server to find chat logs.
		self.is_group_chat = is_group_chat
		self.chat_log = self.start_chat_log()  # File location of chat log.


	def start_chat_log(self):
		# Pretend that the chat log is like the chat window.
		if self.is_group_chat:
			file_name = 'group_chat_logs/' + str(self.chat_id) + '.txt'
		else:
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


	def list_participants(self):
		participants_list = ''
		for user in self.participants:
			if len(participants_list) > 0:
				participants_list += ', '
			participants_list += str(user)

		return participants_list


	def add_participant(self, username):
		# Invoked by the server after someone accepts a group chat invite.
		self.participants.append(username)


	def remove_participant(self, username):
		# When someone leaves the group chat, the UI updates the server, and
		# the server updates the chat object.
		if username in self.participants:
			self.participants.remove(username)

		# When the last user leaves the chat, update the server.
		if len(self.participants) == 0:
			return True
		else:
			return False


	def __str__(self):
		chat_summary = ''

		for participant in self.participants:
			if len(chat_summary) > 0:
				chat_summary += ', '
			chat_summary += str(participant)

		return chat_summary



