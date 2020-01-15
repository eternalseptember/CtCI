"""
Explain the data structures and algorithms that you would use to design an
in-memory file system. Illustrate with an example in code where possible.
"""

# What is the relationship between files and directories?


class entry():
    def __init__(self, name, date_created, date_modified, parent):
        self.name = name
        self.date_created = date_created
        self.date_modified = date_modified
        self.parent = parent


class file():
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory


class directory():
    def __init__(self):
        self.contents = []


