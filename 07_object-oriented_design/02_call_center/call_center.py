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
    employee_type = {0: 'Respondent', 1: 'Manager', 2: 'Director'}

    def __init__(self, employee_id, level=0):
        self.employee_id = employee_id
        self.level = level
        self.in_call = None


    def __str__(self):
        employee = self.employee_type[self.level]
        employee += ' #{0} '.format(self.employee_id)

        if self.in_call is None:
            employee += 'is available.'
        else:
            employee += 'is in call #{0}.\n'.format(self.in_call)

        return employee


    def get_call(self, call_id):
        self.in_call = call_id


    def end_call(self):
        self.in_call = None


    def escalate_call(self):
        escalated_call = self.in_call
        self.in_call = None
        return escalated_call


class Staff_Queue():
    employee_type = {0: 'Respondent', 1: 'Manager', 2: 'Director'}

    def __init__(self, level):
        self.level = level
        self.employees_available = []
        self.assigned_calls = {}
        self.calls_on_hold = []


    def __str__(self):
        queue_str = '{0} Queue:\n'.format(self.employee_type[self.level])
        queue_str += 'Employees available: {0}'.format(self.employees_available)
        queue_str += 'Num of calls on hold: {0}'.format(self.calls_on_hold)
        return queue_str


    def add_employee(self, new_employee):
        # Should get an Employee object
        self.employees_available.append(new_employee)


    def assign_call(self, call_number):
        if len(self.employees_available) == 0:
            # put the call in the queue
            self.calls_on_hold.append(call_number)
        else:
            assigned_employee = self.employees_available.pop(0)
            assigned_employee.get_call(call_number)



class Call_Center():
    def __init__(self):
        self.call_id = 1
        self.employee_id = 1
        self.assigned_calls = {}  # assigned_calls[call_id] = employee_id?
        self.staffers = [Staff_Queue(0), Staff_Queue(1), Staff_Queue(2)]


    def __str__(self):
        # ???
        return str(self.assigned_calls)


    def add_employee(self, level=0):
        new_employee = Employee(self.employee_id, level)
        self.staffers[level].add_employee(new_employee)
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
            forwarding_employee = self.assigned_calls[call_id]


        # New calls are allocated to a respondent who is free first.
        # If all respondents are busy, puts the call in the queue.








