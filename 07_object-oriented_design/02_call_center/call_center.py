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
    def __init__(self, name, level=0):
        self.name = name

        if level == 1:
            self.level = 'manager'
        elif level == 2:
            self.level = 'director'
        else:
            self.level = 'respondent'


        self.status = 'available'
        # other statuses: in call






class Call_Center():
    def __init__(self):
        self.respondent_queue = []
        self.manager_queue = []
        self.director_queue = []

    def add_employee(self, name, level):
        employee = Employee(name, level)
        # add to a queue?


    def dispatch_call(self):
        return None




