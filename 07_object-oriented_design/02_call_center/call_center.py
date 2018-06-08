"""
Imagine you have a call center with three levels of employees: respondent,
manager, and director. An incoming telephone call must be first allocated
to a respondent who is free. If the respondent can't handle the call, he
or she must escalate the call to a manager. If the manager is not free or
not able to handle it, then the call should be escalated to a director.
Design the classes and data structures for this program. Implement a method
dispatchCall() which assigns a call to the first available employee.
"""


class Employee():
    def __init__(self, employee_id, level):
        self.employee_id = employee_id
        self.level = level
        self.in_call = None

    def get_call(self, call_id):
        self.in_call = call_id



class Call_Center():
    def __init__(self):
        self.call_id = 1
        self.employee_id = 1
        self.assigned_calls = {}  # assigned_calls[call_id] = Employee

        # Employees are added to their appropriate queues.
        # Employee.in_call = None
        self.respondent_free = []
        self.manager_free = []
        self.director_free = []

        # List of employees on a call.
        # Employee.in_call = call_id
        self.respondent_in_call = []
        self.manager_in_call = []
        self.director_in_call = []

        # Queues for calls on hold.
        self.respondent_call_queue = []
        self.director_call_queue = []



    def add_employee(self, level=0):
        if level == 1:  # manager
            self.manager_free.append(Employee(self.employee_id, level))
        elif level == 2:  # director
            self.employee_free.append(Employee(self.employee_id, level))
        else:  # respondent
            self.respondent_free.append(Employee(self.employee_id, level))

        self.employee_id += 1


    def dispatch_call(self, call_id=None):
        new_call = False

        # Assign call_id for new calls.
        if call_id is None:
            new_call = True
            call_id = self.call_id
            self.call_id += 1

        # Get information to escalate phone call.
        else:
            employee = self.assigned_calls[call_id]


        if new_call:
            # New calls are allocated to a respondent who is free first.
            if len(self.respondent_free) > 0:
                assigned_respondent = self.respondent.free.pop(0)
                assigned_respondent.in_call = call_id
                self.respondent_in_call.append(assigned_respondent)

            # If all respondents are busy, puts the call in the queue.
            else:
                self.respondent_call_queue.append(call_id)







