from chat import *


from chat_server import *
chat_server = Chat_Server()


participants_1 = ['test_user_1', 'test_user_2']
test_chat_1 = Chat(chat_server, participants_1, 1)
print(test_chat_1)


participants_2 = ['test_user_3', 'test_user_4']
test_chat_2 = Chat(chat_server, participants_2, 2)
print(test_chat_2)
test_chat_2.send_message('test_user_3', 'test message')


participants_3 = ['test_user_1', 'test_user_2', 'test_user_3']
test_chat_3 = Chat(chat_server, participants_3, 1, True)
test_chat_3.send_message('test_user_1', 'group chat test')
test_chat_3.send_message('test_user_3', 'yup')
test_chat_3.send_message('test_user_2', 'test test test')



