"""
Explain the data structures and algorithms that you would use to design an
in-memory file system. Illustrate with an example in code where possible.
"""

# What is the relationship between files and directories?


class Entry():
    def __init__(self, name, date_created, date_modified, parent):
        self.name = name
        self.date_created = date_created
        self.date_modified = date_modified
        self.parent = parent

    def get_full_path(self):
        return

    def rename(self, new_name):
        self.name = new_name


class File(Entry):
    def __init__(self, name, directory, size):
        self.name = name
        self.directory = directory
        self.size = size

    def __str__(self):
        # print full path
        return str(self.name)


class Directory(Entry):
    def __init__(self):
        self.contents = []


