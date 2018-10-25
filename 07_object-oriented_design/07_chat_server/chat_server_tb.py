from chat_server import *


chat_server = Chat_Server()
user1 = User('test_user_1')
user2 = User('test_user_2')
user3 = User('test_user_3')

user1.send_contact_request(chat_server, 'user2')


print(user1)
print(user2)
print(user3)


