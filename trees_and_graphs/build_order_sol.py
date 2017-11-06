"""
Implementing the solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.
"""


class Graph:
    def __init__(self):
        self.nodes = []
        # better name for map
        self.hashmap = {}

    def get_or_create_node(self, name):
        if name not in self.hashmap:
            new_node = Project(name)
            self.nodes.append(new_node)
            # something about map function
        return name

    def add_edge(self, start_name, end_name):
        start = get_or_create_node(start_name)
        end = get_or_create_node(end_name)
        # start.add_neighbor(end)

    def get_nodes(self):
        return self.nodes


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.hashmap = {}
        self.dependencies = 0

    # add neighbor function
    def add_neighbor(self, project_node):
        if project_node.name not in self.hashmap:
            self.children.append(project_node)
            # self.hashmap
            self.dependencies += 1

    def increment_dependencies(self):
        self.dependencies += 1

    def decrement_dependencies(self):
        self.dependencies -= 1


    # not entirely sure these functions are necessary?
    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_num_dependencies(self):
        return self.dependencies





def find_build_order(projects_list, dependencies_list):
    # build graph first
    graph = build_graph(projects_list, dependencies_list)

    # return order_projects()
    return None


def build_graph(projects_list, dependencies):
    """
    Build the graph, adding the edge (a, b) if b is dependent on a.
    Assumes a pair is listed in "build order". The pair (a, b) in
    dependencies indicate that b depends on a and a must be built
    before b.
    """

    return None


def order_projects(projects_list):
    # Return a list of the projets in a correct build order
    return None


def add_non_dependent(project_order, projects_list, offset):
    # Helper function to insert projects with zero dependencies
    # into the project_order array, starting at index offset.
    for project in projects_list:
        if project.get_num_dependencies() == 0:
            project_order[offset] = project
            offset += 1
    return offset




