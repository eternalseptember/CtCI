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
        self.group_chat_requests = {}
        #    self.group_chat_requests[group_chat_id] = [senders]


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
        # Server handles updating the appropriate lists.
        self.server.send_contact_request(self.username, target_contact)


    def update_pending_request(self, target_contact):
        # Invoked by the chat server as a result of send_contact_request().
        self.pending_requests.append(target_contact)


    def receive_contact_request(self, sender):
        # Invoked by the chat server as a result of send_contact_request().
        self.received_requests.append(sender)


    def confirm_contact_request(self, sender):
        # Invoked by the chat server as a result of check_contact_requests().
        self.clean_contact_request_lists(sender)
        self.confirmed_contacts.append(sender)
        self.confirmed_contacts.sort()


    def deny_contact_request(self, sender):
        # Invoked by the chat server as a result of check_contact_requests().
        self.clean_contact_request_lists(sender)


    def clean_contact_request_lists(self, sender):
        # Helper function.
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

            # Checks whether this user can participate in this group chat.
            if chat_id not in self.group_chat_history:
                print('Cannot participate in this chat.')
                return None

        else:
            # 'participants' argument can either be a list of participants
            # (if it's a new chat, then there will be no chat id)
            # or the chat id of an existing chat.
            if type(participants) is list:
                # THIS IS THE ONLY WAY TO START A SIMPLE CHAT WITH ONE OTHER PERSON!
                # Checking that the chat recipients are in the user's contacts list.
                unconfirmed_contacts = []

                for participant in participants:
                    if not self.in_contacts_list(participant):
                        unconfirmed_contacts.append(participant)

                # Remove unconfirmed contacts from the chat participants list.
                for contact in unconfirmed_contacts:
                    participants.remove(contact)

                # Add the user to the chat participants list for chat lookups.
                if self.username not in participants:
                    participants.append(self.username)

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
        print('Starting group chat.')
        self.group_chat_history.append(group_chat_id)

        # Send an invitation to everybody.
        for participant in participants:
            self.invite_to_group_chat(group_chat_id, participant)

        return group_chat_id


    def invite_to_group_chat(self, group_chat_id, participant):
        # The sender should send this from a group chat window.
        # All of the participants should be in the user's contacts list.
        if not self.in_contacts_list(participant):
            print('{0} is not in your confirmed contacts list.'.format(participant))
            return False

        # Check if the group chat is valid?
        self.server.invite_to_group_chat(group_chat_id, self.username, participant)



    def invited_to_group_chat(self, group_chat_id, sender):
        # Invoked by the server as a result of __start_group_chat()__.
        if group_chat_id not in self.group_chat_requests:
            self.group_chat_requests[group_chat_id] = [sender]
        else:
            people_who_invited = self.group_chat_requests[group_chat_id]

            # In case someone sends the same invitation multiple times
            if sender not in people_who_invited:
                people_who_invited.append(sender)


    def enter_group_chat(self, group_chat_id, chat_ongoing):
        # Invoked by the server as a result of check_group_chat_invites().
        if chat_ongoing:
            self.group_chat_history.append(group_chat_id)
            print('Entering group chat.')
        else:
            print('This group chat has been closed.')

        if group_chat_id in self.group_chat_requests:
            del self.group_chat_requests[group_chat_id]


    def reject_group_chat(self, group_chat_id):
        # Invoked by the server as a result of check_group_chat_invites().
        if group_chat_id in self.group_chat_requests:
            del self.group_chat_requests[group_chat_id]


    def leave_group_chat(self, group_chat_id):
        # Invoked by the user.
        self.server.leave_group_chat(group_chat_id, self.username)


    def check_group_chat_invites(self):
        # Invoked by the user.
        accepted = []
        denied = []

        # UPDATE THIS FOR MULTILPE INVITATIONS TO THE SAME CHAT!!!
        group_chats = self.group_chat_history.keys()
        for group_chat_id in group_chats:
            acceptable_choices = ['Y', 'N', 'S']
            answer = ''

            # Formatting the list of group chat inviters.
            senders = self.group_chat_history[group_chat_id]
            senders_list = ''
            for sender in senders:
                if len(senders_list) > 0:
                    senders_list += ', '
                senders_list += str(sender)

            # Format the list of people in the chat.
            users_in_chat = self.server.list_users_in_chat(group_chat_id, True)
            users_list = ''
            for user in users_in_chat:
                if len(users_list) > 0:
                    users_list += ', '
                users_list += str(user)

            print('You are invited to a group chat by {0}.'.format(senders_list))
            print('People in this chat: {0}'.format(users_in_chat))

            # Accept or reject.
            while (answer not in acceptable_choices):
                print('Press Y to accept this group chat invitation, \
                    N to decline, or S to skip.')

                answer = input()

            if answer.upper() == 'Y':
                print('entering chat')
                accepted.append(group_chat_id)

            elif answer.upper() == 'N':
                print('decline to chat')
                denied.append(group_chat_id)

            elif answer.upper() == 'S':
                print('skipping this chat')

        # Chat server send and update requests.
        for group_chat_id in accepted:
            self.server.enter_group_chat(self.username, group_chat_id)
        for group_chat_id in denied:
            self.server.reject_group_chat(self.username, group_chat_id)










