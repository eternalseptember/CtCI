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
			list_of_routes.append(route.data)

		return 'name: {0}\t\troutes: {1}'.format(self.name, list_of_routes)


def has_route_between_nodes(from_node, to_node):
	# return True if there is a route between the two
	# return False if there isn't a route
	return None



# first graph
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
print()

# test case 2: false
result = has_route_between_nodes(node3, node0)
print(result)
print()

