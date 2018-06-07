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
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.in_call = None

    def get_call(self, call_id):
        self.in_call = call_id



class Call_Center():
    def __init__(self):
        self.respondent_free = []
        self.respondent_in_call = []
        self.manager_free = []
        self.manager_in_call = []
        self.director_free = []
        self.director_in_call = []


    def add_employee(self, name, level=0):
        if level == 1:
            employee_level = 'manager'
        elif level == 2:
            employee_level = 'director'
        else:
            employee_level = 'respondent'

        employee = Employee(name, employee_level)


        # add to a queue?


    def dispatch_call(self):
        return None




