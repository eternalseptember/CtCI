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
        self.assigned_calls = {}  # assigned_calls[call_id] = staff_assigned
        self.calls_on_hold = []


    def __str__(self):
        queue_str = '{0} Queue:\n'.format(self.employee_type[self.level])

        for call in self.assigned_calls.keys():
            active_call = 'Call #{0} is received by Employee #{1}\n'.format(call, self.assigned_calls[call])
            queue_str += active_call

        queue_str += 'Employees available: {0}\n'.format(self.employees_available)
        queue_str += 'Num of calls on hold: {0}\n'.format(self.calls_on_hold)
        return queue_str


    def add_employee(self, new_employee):
        self.employees_available.append(new_employee)


    def assign_call(self, call_id):
        # NEED TO CHECK AND ASSIGN CALLS ON HOLD.
        if len(self.employees_available) > 0:
            assigned_employee = self.employees_available.pop(0)
            self.assigned_calls[call_id] = assigned_employee
        else:
            self.calls_on_hold.append(call_id)


    def end_call(self, call_id):
        employee = self.assigned_calls[call_id]
        self.employees_available.append(employee)
        del self.assigned_calls[call_id]


    def escalate_call(self, call_id):
        self.end_call(call_id)
        return call_id



class Call_Center():
    def __init__(self):
        self.call_id = 1
        self.employee_id = 1
        self.assigned_calls = {}  # assigned_calls[call_id] = staff_level_num
        self.staff_levels = [Staff_Queue(0), Staff_Queue(1), Staff_Queue(2)]


    def __str__(self):
        staff_summary = ''

        for staff_list in self.staff_levels:
            staff_summary += str(staff_list)
            staff_summary += '\n'

        return staff_summary


    def add_employee(self, level=0):
        self.staff_levels[level].add_employee(self.employee_id)
        self.employee_id += 1


    def new_call(self):
        call_id = self.call_id
        self.call_id += 1
        return self.dispatch_call(call_id)


    def end_call(self, call_id):
        queue = self.assigned_calls[call_id]

        # go into staff_levels queue and clean up employees
        return None


    def escalate_call(self, call_id):
        return self.dispatch_call(call_id)


    def dispatch_call(self, call_id):
        # New and escalated calls use this function.
        # New calls are allocated to a respondent who is free first.
        if call_id not in self.assigned_calls:
            self.assigned_calls[call_id] = 0
            return self.staff_levels[0].assign_call(call_id)
        else:
            prev_level = self.assigned_calls[call_id]
            next_level = prev_level + 1
            self.assigned_calls[call_id] = next_level
            return self.staff_levels[next_level].assign_call(call_id)









