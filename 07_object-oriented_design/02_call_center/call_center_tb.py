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

# Testing new calls
for i in range(17):
    call_center.new_call()

# print(call_center)
# print()


# Testing sequences
# End first call.
call_center.end_call(1, False)

# Escalate these calls.
for call in range(2, 9):
    call_center.end_call(call, True)

# There's no queue for managers, but there's a queue for directors.

# Some escalated calls end.
escalated_calls = [2, 4, 7]
for call in escalated_calls:
    call_center.end_call(call, False)



