# User objects used in chat server program.


class User():
    def __init__(self, username):
        self.username = username
        self.status_message = ''
        self.contacts = []
        self.sent_requests = []
        self.received_requests = []  # Requests sent by others. Accept or deny.


    def update_status(self, status_message):
        self.status_message = status_message


    def send_contact_request(self, chat_server, target_contact):
        # Send contact request through the server.
        req = chat_server.send_contact_request(str(self.username), target_contact)

        # Append to sent_requests list after chat server returns true.
        if req:
            self.sent_requests.append(target_contact)


    def receive_contact_request(self, sender):
        self.received_requests.append(sender)


    def check_contact_requests(self, chat_server, sender):
        for request in self.receive_requests:
            print('{0} sent a contact request. \
                Press 1 to accept, 2 to deny, and 3 to skip. '.format(request))

            answer = input()
            if answer == 1:
                print('accepted')
            elif answer == 2:
                print('denied')
            else:
                print('skipped')

        return False


    def __str__(self):
        summary = '{0}\n'.format(self.username)

        contacts_list = ''
        for contact in self.contacts:
            if len(contacts_list) > 0:
                contacts_list += ', '
            contacts_list += str(contact)

        sent_list = ''
        for contact in self.sent_requests:
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

