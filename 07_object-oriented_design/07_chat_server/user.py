# User objects used in chat server program.


class User():
    def __init__(self, username):
        self.username = username
        self.online_status = ''
        self.status_message = ''
        self.confirmed_contacts = []
        self.pending_requests = []
        self.received_requests = []  # Requests sent by others.
        self.server = None
        self.chat_history = []  # List of simple chats the user is in.
        self.group_chat_history = []  # Keep this to access group chat logs.
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
        self.server = server
        self.online_status = 'Online'


    def logout(self):
        self.server = None
        self.online_status = 'Offline'


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


    def chat(self, participants, message, is_group_chat=False):
        if is_group_chat:
            # 'participants' argument will be the group chat id.
            chat_id = participants

            if chat_id not in self.group_chat_history:
                self.group_chat_history.append(chat_id)

        else:
            # 'participants' argument can either be a list of participants
            # (if it's a new chat, then there will be no chat id)
            # or the chat id of an existing chat.
            if type(participants) is list:
                # THIS IS THE ONLY WAY TO START A SIMPLE CHAT WITH ONE OTHER PERSON.
                # Checking that the chat recipients are in the user's contacts list.
                unconfirmed_contacts = []

                for participant in participants:
                    if not self.in_contacts_list(participant):
                        unconfirmed_contacts.append(participant)

                # Remove unconfirmed contacts from the chat participants list.
                for contact in unconfirmed_contacts:
                    participants.remove(contact)

                # Add the user to the chat participants list for chat lookups.
                if str(self.username) not in participants:
                    participants.append(str(self.username))

                # If there are no valid chat participants.
                if len(participants) == 1:
                    print('No valid chat participants.')
                    return None

                participants.sort()
                participants = tuple(participants)

                # If a new chat needs to be set up, it'll be done here.
                chat_id = self.server.start_chat(participants)

            elif type(participants) is int:
                chat_id = participants

            if chat_id not in self.chat_history:
                    self.chat_history.append(chat_id)


        self.server.send_message(chat_id, self.username, message, is_group_chat)

        return chat_id


# *****************************************************************************


    def start_group_chat(self, participants):
        # THIS IS THE ONLY WAY TO START A GROUP CHAT!
        # The person who started the group chat will be the first participant.
        group_chat_id = self.server.start_group_chat(self.username)

        # Send an invitation to everybody.
        # All of the participants should be in the user's contacts list.
        

        print('starting group chat')



    def invite_to_group_chat(self, request):
        # Invoked by the server.
        # request = (sender, group_chat_id)
        self.group_chat_requests.append(request)


    def reject_group_chat(self, request):
        # request = (sender, group_chat_id)
        # Update the server's group chat request log.
        # Clean up user's group chat invitations list.
        print('not entering the group chat')


    def enter_group_chat(self, request):
        # request = (sender, group_chat_id)
        # Update the server's group chat request log.
        # Clean up user's group chat invitations list.
        print('append group chat history with new chat id')


    def leave_group_chat(self, group_chat_id):
        # Update the server.
        print('leaving a group chat')


    def check_group_chat_invites(self):
        for request in self.group_chat_requests:
            acceptable_choices = ['Y', 'N', 'S']
            answer = ''

            sender, group_chat_id = (request)
            print('You\'ve been invited to a group chat by {0}.'.format(sender))
            # Print info about the chat,
            # like who sent the invite and who's in the chat room.

            # Accept or reject.
            while (answer not in acceptable_choices):
                print('Press Y to accept this group chat invitation, \
                    N to decline, or S to skip.')

                answer = input()

            # should probably check if the group chat is still happening
            # when they accept the invitation

            if answer.upper() == 'Y':
                print('entering chat')
                self.enter_group_chat(request)

            elif answer.upper() == 'N':
                print('decline to join chat')
                self.reject_group_chat(request)

            elif answer.upper() == 'S':
                print('skipping this chat')


        # Chat server send and update requests.










