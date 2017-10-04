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



# Graph 1
node0 = Node('node0')
node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')

node0.routes = [node1, node2]
node1.routes = [node2]
node2.routes = [node0, node3]
node3.routes = [node3]

# test case 1: true
result = has_route_between_nodes(node1, node3)
print(result)

# test case 2: false
result = has_route_between_nodes(node3, node0)
print(result)
print()


# Graph 2
node0 = Node('node0')
node1 = Node('node1')
node2 = Node('node2')

node0.routes = [node1]
node1.routes = [node2]

# test case 3: false
result = has_route_between_nodes(node2, node1)
print(result)

# test case 4: false
result = has_route_between_nodes(node2, node0)
print(result)

# test case 5: false
result = has_route_between_nodes(node1, node0)
print(result)

# test case 6: true
# Answer key assumes this to be true even if there isn't
# a node pointing back to itself.
result = has_route_between_nodes(node0, node0)
print(result)

# test case 7: true
result = has_route_between_nodes(node0, node1)
print(result)

# test case 8: true
result = has_route_between_nodes(node0, node2)
print(result)

# test case 9: true
result = has_route_between_nodes(node1, node2)
print(result)
print()


# Graph 3
nodeA = Node('nodeA')
nodeB = Node('nodeB')
nodeC = Node('nodeC')
nodeD = Node('nodeD')

nodeA.routes = [nodeB, nodeD]
nodeB.routes = [nodeC]
nodeC.routes = [nodeA]

# test case 10: true
result = has_route_between_nodes(nodeA, nodeC)
print(result)

# test case 11: true
result = has_route_between_nodes(nodeB, nodeD)
print(result)

# test case 12: false
result = has_route_between_nodes(nodeD, nodeC)
print(result)



