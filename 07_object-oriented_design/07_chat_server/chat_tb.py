from chat import *


participants_1 = ['test_user_1', 'test_user_2']
test_chat_1 = Chat(participants_1, 1)
print(test_chat_1)


participants_2 = ['test_user_3', 'test_user_4']
test_chat_2 = Chat(participants_2, 2)
print(test_chat_2)
test_chat_2.send_message('test_user_3', 'test message')



