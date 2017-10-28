"""
Implementing the solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.
"""


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


