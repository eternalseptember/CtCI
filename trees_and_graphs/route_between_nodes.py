"""
Given a directed graph, design an algorithm to find out whether there is
a route between two nodes.
"""

class Node():
	def __init__(self, data=None, routes=None):
		self.data = data
		
		if routes is None:
			self.routes = []
		else:
			self.routes = routes


	def __str__(self):
		list_of_routes = []

		for route in self.routes:
			list_of_routes.append(route.data)

		return 'data: {0}\nroutes: {1}'.format(self.data, list_of_routes)




