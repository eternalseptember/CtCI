from call_center import *


employee_1 = Employee(6, 0)
print(employee_1)


employee_2 = Employee(7, 1)
employee_2.get_call(3)
print(employee_2)
escalated_call = employee_2.escalate_call()
print('escalated call: {0}'.format(escalated_call))
print(employee_2)






"""
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
"""

