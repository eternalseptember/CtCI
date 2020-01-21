"""
Explain the data structures and algorithms that you would use to design an
in-memory file system. Illustrate with an example in code where possible.
"""

# What is the relationship between files and directories?


class Entry():
    def __init__(self, name, parent, date_created, date_modified):
        self.name = name
        self.parent = parent
        self.date_created = date_created
        self.date_modified = date_modified


    def get_full_path(self):
        if self.parent is None:
            return self.name
        # else get the parent's name and then add this name

    def rename(self, new_name):
        self.name = new_name


class File(Entry):
    def __init__(self, name, directory, date_created, date_modified, size):
        # have to spell out None if there's no parent directory
        Entry.__init__(self, name, directory, date_created, date_modified)
        self.size = size


    def __str__(self):
        # print full path
        return str(self.name)


class Directory(Entry):
    def __init__(self):
        self.contents = []


