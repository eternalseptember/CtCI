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


