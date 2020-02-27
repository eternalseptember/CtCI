"""
Explain the data structures and algorithms that you would use to design an
in-memory file system. Illustrate with an example in code where possible.
"""

# What is the relationship between files and directories?


class Entry():
    """
    def __init__(self, name, parent_dir, date_created, date_modified):
        self.name = name
        self.parent_dir = parent_dir  # directory object
        self.date_created = date_created
        self.date_modified = date_modified
    """

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir  # directory object

        # there should be error checking here.
        if parent_dir is not None:
            parent_dir.add_entry(self)


    def get_full_path(self):
        if self.parent_dir is None:
            return self.name
        else:
            return '{0}/{1}'.format(self.parent_dir.get_full_path(), self.name)


    def rename(self, new_name):
        self.name = new_name


    def __str__(self):
        return str(self.name)


class File(Entry):
    """
    def __init__(self, name, parent_dir, date_created, date_modified, size):
        # have to spell out None if there's no parent directory
        Entry.__init__(self, name, parent_dir, date_created, date_modified)
        self.size = size
    """

    def __init__(self, name, parent_dir, size):
        Entry.__init__(self, name, parent_dir)
        self.size = size


class Directory(Entry):
    def __init__(self, name, parent_dir):
        Entry.__init__(self, name, parent_dir)
        self.contents = []
        self.num_of_items = 0


    def add_entry(self, item):
        if item in self.contents:
            print('File with that name exists.')
            return False
        else:
            self.contents.append(item)
            self.num_of_items += 1
            return True


    def delete_entry(self, item, file_type):
        try:
            entry = (item, file_type)
            self.contents.remove(entry)
            self.num_of_items -= 1
        except:
            print('File or folder does not exist.')


    def get_contents(self):
        content_str = ''

        for content in self.contents:
            content_str += str(content)
            content_str += '\n'

        print(content_str)


    def get_num_of_items(self):
        return self.num_of_items




