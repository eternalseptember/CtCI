"""
Given a directed graph, design an algorithm to find out whether there is
a route between two nodes.
"""


class Node():
    def __init__(self, name=None, routes=None):
        self.name = name
        self.routes = []

        if routes is not None:
            for item in routes:
                self.routes.append(item)


    def __str__(self):
        list_of_routes = []

        for route in self.routes:
            list_of_routes.append(route.name)

        return 'name: {0}\t\troutes: {1}'.format(self.name, list_of_routes)


def has_route_between_nodes(from_node, to_node):
    # return True if there is a route between the two
    # return False if there isn't a route

    if from_node == to_node:
        return True

    visited = []
    queue = [from_node]

    if from_node == to_node:
        return True

    while len(queue) > 0:
        current_node = queue.pop(0)

        for route in current_node.routes:
            if route == to_node:
                return True
            else:
                if (route not in queue) and (route not in visited):
                    queue.append(route)

        # record node as visited if there isn't a path
        visited.append(current_node)


    return False

