"""
Imagine you have a call center with three levels of employees: respondent,
manager, and director. An incoming telephone call must be first allocated
to a respondent who is free. If the respondent can't handle the call, he
or she must escalate the call to a manager. If the manager is not free or
not able to handle it, then the call should be escalated to a director.
Design the classes and data structures for this program. Implement a method
dispatchCall() which assigns a call to the first available employee.
"""


class Staff_Queue():
    employee_type = {0: 'Respondent', 1: 'Manager', 2: 'Director'}

    def __init__(self, level):
        self.level = level
        self.employees_available = []
        self.assigned_calls = {}
        self.calls_on_hold = []


    def __str__(self):
        queue_str = '{0} Queue:\n'.format(self.employee_type[self.level])
        queue_str += 'Employees available: {0}\n'.format(self.employees_available)
        queue_str += 'Num of calls on hold: {0}\n'.format(self.calls_on_hold)
        return queue_str


    def add_employee(self, new_employee):
        self.employees_available.append(new_employee)


    def add_call_to_queue(self, call_number):
        # Calls will be answered in order.
        self.calls_on_hold.append(call_number)


    def assign_call(self, call_number):
        if len(self.employees_available) > 0:
            assigned_employee = self.employees_available.pop(0)
            self.assigned_calls[call_number] = assigned_employee


    def end_call(self, call_number):
        employee = self.assigned_calls[call_number]
        self.employees_available.append(employee)
        del self.assigned_calls[call_number]


    def escalate_call(self):
        # return the call number
        return None



class Call_Center():
    def __init__(self):
        self.call_id = 1
        self.employee_id = 1
        self.assigned_calls = {}
        self.staffers = [Staff_Queue(0), Staff_Queue(1), Staff_Queue(2)]


    def __str__(self):
        queue_list = ''

        for staff_list in self.staffers:
            queue_list += str(staff_list)
            queue_list += '\n'

        return queue_list


    def add_employee(self, level=0):
        self.staffers[level].add_employee(self.employee_id)
        self.employee_id += 1


    def new_call(self):
        call_id = self.call_id
        self.call_id += 1

        return self.dispatch_call(call_id)



    def dispatch_call(self, call_id=None):
        # This function runs for new calls and escalated calls.

        # New calls are allocated to a respondent who is free first.
        # If all respondents are busy, puts the call in the queue.








