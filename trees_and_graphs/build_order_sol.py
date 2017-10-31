"""
Implementing the solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.
"""


class graph():
    def __init__():
        self.nodes = []
        self.map = {}

    def get_or_create_node(self, name):
        # stuff here
        # return map.get(name)
        return name

    def add_edge(self, start_name, end_name):
        start = get_or_create_node(start_name)
        end = get_or_create_node(end_name)
        # start.add_neighbor(end)



    def get_nodes(self):
        return self.nodes



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
    # Helper functio nto insert projects with zero dependencies
    # into the project_order array, starting at index offset.
    return offset

