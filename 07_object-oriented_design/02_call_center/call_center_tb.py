from call_center import *


call_center = Call_Center()

# Add 10 respondents
for i in range(10):
    call_center.add_employee()

# Add 4 managers
for i in range(4):
    call_center.add_employee(1)

# Add 2 directors
for i in range(2):
    call_center.add_employee(2)

# print('After adding employees in call center.')
# print(call_center)


# Testing call
print('New calls.')
for i in range(13):
    call_center.new_call()
print(call_center)

# Testing end call


# Testing escalate call


