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
    levels = ['respondent', 'manager', 'director']
    status = ['available', 'in call']

    def __init__(self, name, level):
        self.name = name
        self.level = level




class Call_Center():
    def __init__(self):
        self.respondent_queue = []
        self.manager_queue = []
        self.director_queue = []


    def dispatch_call():
        return None




