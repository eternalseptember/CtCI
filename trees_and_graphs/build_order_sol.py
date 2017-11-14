"""
Implementing the solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.
"""


class Graph:
    def __init__(self):
        self.nodes = []
        self.node_map = {}

    def get_or_create_node(self, name):
        if name not in self.node_map:
            new_node = Project(name)
            self.nodes.append(new_node)
            self.node_map[name] = new_node
        # better way of returning that node?
        return self.node_map[name]

    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)

    def get_nodes(self):
        return self.nodes

    def print_nodes(self):
        return str(self.nodes)

    def print_nodes_map(self):
        return str(self.node_map)


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.node_map = {}
        self.dependencies = 0

    # add neighbor function
    def add_neighbor(self, new_node):
        if new_node.name not in self.node_map:
            self.children.append(new_node)
            self.node_map[new_node.name] = new_node
            new_node.increment_dependencies()

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

    # print things
    def print_name(self):
        return str(self.name)

    def print_children(self):
        return str(self.children)

    def print_node_map(self):
        return str(self.node_map)

    def print_num_of_dep(self):
        return str(self.dependencies)




def find_build_order(projects_list, dependencies_list):
    # build graph first
    graph = build_graph(projects_list, dependencies_list)
    return order_projects(graph.get_nodes())


def build_graph(projects_list, dependencies):
    """
    Build the graph, adding the edge (a, b) if b is dependent on a.
    Assumes a pair is listed in "build order". The pair (a, b) in
    dependencies indicate that b depends on a and a must be built
    before b.
    """
    graph = Graph()
    for project in projects_list:
        # ???
        graph.get_or_create_node(project)

    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph


def order_projects(projects_list):
    # Return a list of the projets in a correct build order
    project_order = []

    # Add "roots" to the build order first.
    end_of_list = add_non_dependent(project_order, projects_list, 0)

    to_be_processed = 0

    # length ???
    while to_be_processed < len(project_order):
        current = project_order[to_be_processed]

        # We have a circular dependency since there are no remaining projects
        # with zero dependencies.
        if current is None:
            return None

        # Remove (current project?) as dependency


        # Add children that have no one depending on them


    return order


def add_non_dependent(project_order, projects_list, offset):
    # Helper function to insert projects with zero dependencies
    # into the project_order array, starting at index offset.
    for project in projects_list:
        if project.get_num_dependencies() == 0:
            project_order[offset] = project
            offset += 1
    return offset




