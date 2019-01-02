# User objects used in chat server program.


class User():
    def __init__(self, username):
        self.username = username
        self.status_message = ''
        self.confirmed_contacts = []
        self.pending_requests = []
        self.received_requests = []  # Requests sent by others.
        self.server = None
        self.chat_history = []  # List of simple chats the user is in.
        self.group_chat_history = []
        self.group_chat_requests = []  # (sender, group_chat_id)


    def __str__(self):
        return str(self.username)


    def __repr__(self):
        return str(self.username)


    def print_user_summary(self):
        if len(self.status_message) > 0:
            summary = '{0} - {1}\n'.format(self.username, self.status_message)
        else:
            summary = '{0}\n'.format(self.username)

        contacts_list = ''
        for contact in self.confirmed_contacts:
            if len(contacts_list) > 0:
                contacts_list += ', '
            contacts_list += str(contact)

        pending_list = ''
        for contact in self.pending_requests:
            if len(pending_list) > 0:
                pending_list += ', '
            pending_list += str(contact)

        received_list = ''
        for contact in self.received_requests:
            if len(received_list) > 0:
                received_list += ', '
            received_list += str(contact)

        summary += 'Contacts list: '
        summary += '{0}\n'.format(contacts_list)
        summary += 'Pending list: '
        summary += '{0}\n'.format(pending_list)
        summary += 'Received list: '
        summary += '{0}\n'.format(received_list)

        print(summary)


# *****************************************************************************


    def login(self, server):
        # Logging in.
        self.server = server


    def update_status(self, status_message):
        self.status_message = status_message


# *****************************************************************************


    def send_contact_request(self, target_contact):
        # Invoked by the user.
        # Send contact request through the server.
        self.server.send_contact_request(self.username, target_contact)


    def update_pending_request(self, target_contact):
        # Invoked by the chat server.
        self.pending_requests.append(target_contact)


    def receive_contact_request(self, sender):
        # Invoked by the chat server.
        self.received_requests.append(sender)


    def confirm_contact_request(self, sender):
        # Invoked by the chat server.
        if sender in self.pending_requests:
            self.pending_requests.remove(sender)
        if sender in self.received_requests:
            self.received_requests.remove(sender)

        self.confirmed_contacts.append(sender)


    def deny_contact_request(self, sender):
        # Invoked by the chat server.
        if sender in self.pending_requests:
            self.pending_requests.remove(sender)
        if sender in self.received_requests:
            self.received_requests.remove(sender)


    def check_contact_requests(self):
        # Invoked by the user.
        accepted = []
        denied = []

        # Requests could be listed in a form.
        for request in self.received_requests:
            acceptable_choices = ['1', '2', '3']
            answer = ''

            while (answer not in acceptable_choices):
                print('{0} sent a contact request to {1}. \
                    {1}: Press 1 to accept, 2 to deny, or 3 to skip.'
                    .format(request, self.username))

                answer = input()

            if answer == '1':
                print('{0} accepted {1}.'.format(self.username, request))
                accepted.append(request)
            elif answer == '2':
                print('{0} denied {1}.'.format(self.username, request))
                denied.append(request)
            elif answer == '3':
                print('{0} skipped {1}.'.format(self.username, request))

        # Update statuses of requests.
        for request in accepted:
            self.server.accept_contact_request(self.username, request)
        for request in denied:
            self.server.deny_contact_request(self.username, request)


    def in_contacts_list(self, other_user):
        # Check that other_user is in THIS user's confirmed contacts list.
        if other_user in self.confirmed_contacts:
            return True
        else:
            return False


# *****************************************************************************


    def chat(self, participants, message):
        # is_group_chat = False
        # The data type of 'participants' argument determines the chat type.
        # If 'participants' is a list, then it will be a normal chat.
        # Group chats can only be passed by group_id.
        #

        # Two-party chat, but could be used for group-chat.
        if type(participants) is list:
            if str(self.username) not in participants:
                participants.append(str(self.username))
            participants.sort()
            participants = tuple(participants)

            chat_id = self.server.get_chat_id(participants)
            is_group_chat = False

            if chat_id not in self.chat_history:
                self.chat_history.append(chat_id)

        # In this solution, group chats can only be passed by group_id.
        elif type(participants) is int:
            chat_id = participants
            is_group_chat = True

            if chat_id not in self.group_chat_history:
                self.group_chat_history.append(chat_id)

        self.server.send_message(chat_id, self.username, message)

        return chat_id, is_group_chat


# *****************************************************************************


    def invite_to_chat(self, current_chat_id, invited_user):
        # Single chat and group chat use different numbering systems, in case
        # someone invites multiple people to the group chat at the same time.


        group_chat_id = self.server.get_group_chat_id(current_chat_id)

        chat_invite_num = self.server.invite_to_group_chat(
            group_chat_id, self.username, invited_user
            )

        return group_chat_id, chat_invite_num


    def check_invite_status(self, chat_invite_num):
        # Query the server to see if invited user accepted chat request.
        # Although the user interface could just query the chat's participants
        # list, and if the user accepted, then their username will show up.
        return self.server.check_invite_status(chat_invite_num)


    def update_group_chat_request(self, request):
        # Invoked by the server.
        # request = (sender, old_chat_id)
        # old_chat_id is for the group already formed.
        # If the user accepts, there will be a new chat_id.
        self.group_chat_requests.append(request)


    def accept_chat_invite(self, chat_id):
        # update server,
        # clean up group chat requests

        print('append chat history with new chat id')


    def check_group_chat_invites(self):
        for chat_id in self.group_chat_requests:
            print('chat request: {0}'.format(chat_id))
        # Accept or reject.

        # Print info about the chat,
        # like who sent the invite and who's in the chat room.

        # Chat server send and update requests.










