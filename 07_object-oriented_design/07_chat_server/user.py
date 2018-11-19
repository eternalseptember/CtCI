# User objects used in chat server program.


class User():
    def __init__(self, username):
        self.username = username
        self.status_message = ''
        self.confirmed_contacts = []
        self.pending_requests = []
        self.received_requests = []  # Requests sent by others. Accept or deny.
        self.server = None


    def login(self, server):
        # Logging in.
        self.server = server


    def update_status(self, status_message):
        self.status_message = status_message


    def send_contact_request(self, target_contact):
        # Send contact request through the server.
        req = self.server.send_contact_request(self.username, target_contact)

        # Append to pending_requests list after chat server returns true.
        if req:
            self.pending_requests.append(target_contact)


    def receive_contact_request(self, sender):
        # Called by the server.
        self.received_requests.append(sender)


    def confirm_contact_request(self, sender):
        # Called by the server.
        if sender in self.pending_requests:
            self.pending_requests.remove(sender)
        if sender in self.received_requests:
            self.received_requests.remove(sender)

        self.confirmed_contacts.append(sender)


    def deny_contact_request(self, sender):
        # Called by the server.
        if sender in self.pending_requests:
            self.pending_requests.remove(sender)
        if sender in self.received_requests:
            self.received_requests.remove(sender)


    def check_contact_requests(self):
        accepted = []
        denied = []

        for request in self.received_requests:
            answer = ''
            acceptable_choices = ['1', '2', '3']

            while (answer not in acceptable_choices):
                print('{0} sent a contact request. \
                    Press 1 to accept, 2 to deny, and 3 to skip. '.format(request))

                answer = input()

            if answer == '1':
                print('accepted {0}'.format(request))
                accepted.append(request)
            elif answer == '2':
                print('denied {0}'.format(request))
                denied.append(request)
            elif answer == '3':
                print('skipped {0}'.format(request))

        for request in accepted:
            self.server.accept_contact_request(self.username, request)

        for request in denied:
            self.server.deny_contact_request(self.username, request)


    def chat(self, participant, message):
        # two party chat for now
        # check that the participant is in the contact list?

        # begin chat by finding or starting a chat log with the participant
        # return id of chat
        # then send message with id of chat
        self.server.begin_chat(self.username, participant)


    def print_user_summary(self):
        summary = '{0} - {1}\n'.format(self.username, self.status_message)

        contacts_list = ''
        for contact in self.confirmed_contacts:
            if len(contacts_list) > 0:
                contacts_list += ', '
            contacts_list += str(contact)

        sent_list = ''
        for contact in self.pending_requests:
            if len(sent_list) > 0:
                sent_list += ', '
            sent_list += str(contact)

        received_list = ''
        for contact in self.received_requests:
            if len(received_list) > 0:
                received_list += ', '
            received_list += str(contact)

        summary += 'Contacts list: '
        summary += '{0}\n'.format(contacts_list)
        summary += 'Sent list: '
        summary += '{0}\n'.format(sent_list)
        summary += 'Received list: '
        summary += '{0}\n'.format(received_list)

        return summary


    def __str__(self):
        return str(self.username)



