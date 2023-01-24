"""
Implementing the solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.
"""


class Graph:
	def __init__(self):
		self.projects_list = []
		self.projects_map = {}

	# Each 'project' is a node.
	def get_or_create_project(self, project_name):
		if project_name not in self.projects_map:
			new_project = Project(project_name)
			self.projects_list.append(new_project)
			self.projects_map[project_name] = new_project
		return self.projects_map[project_name]

	# Each 'dependency' is an edge.
	def add_dependency(self, start_name, end_name):
		build_first = self.get_or_create_project(start_name)
		build_second = self.get_or_create_project(end_name)
		build_first.add_edge(build_second)

	def get_projects(self):
		return self.projects_list

	# Print things.
	def print_projects_list(self):
		return str(self.projects_list)

	def print_projects_map(self):
		return str(self.projects_map)

	def __str__(self):
		graph_str = 'Projects (nodes) in this graph:\n'
		graph_str += self.print_projects_list()
		# graph_str += '\n\nProjects Map\n'
		# graph_str += self.print_projects_map()
		return graph_str


class Project:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.node_map = {}
		self.dependencies = 0

	def add_edge(self, new_node):
		if new_node.name not in self.node_map:
			self.children.append(new_node)
			self.node_map[new_node.name] = new_node
			new_node.increment_dependencies()

	def increment_dependencies(self):
		self.dependencies += 1

	def decrement_dependencies(self):
		self.dependencies -= 1

	def get_num_dependencies(self):
		return self.dependencies

	def get_children(self):
		return self.children

	# Print things.
	def __str__(self):
		return 'Project {0}'.format(self.name)

	def __repr__(self):
		return self.name
		#return '{0}'.format(self.name)

	def print_project_details(self):
		project_str = '\tProject {0}\n'.format(self.name)
		project_str += 'Num of prerequisites for this project: \t{0}\n'.format(self.dependencies)
		project_str += 'This project is a prerequisite for: \t{0}\n'.format(self.children)
		# project_str += 'This project\'s node map: {0}\n'.format(self.node_map)
		print(project_str)


def find_build_order(projects_list, dependencies_list):
	# Build graph first.
	graph = build_graph(projects_list, dependencies_list)
	return order_projects(graph.get_projects())


def build_graph(projects_list, dependencies_list):
	"""
	Build the graph, adding the edge (a, b) if b is dependent on a.
	Assumes a pair is listed in "build order". The pair (a, b) in
	dependencies indicate that b depends on a and a must be built
	before b.
	"""
	graph = Graph()

	# Each 'project' is a node in the graph.
	for project in projects_list:
		graph.get_or_create_project(project)

	# Each 'edge' establishes a dependency.
	for dependency in dependencies_list:
		build_first, build_second = (dependency)
		graph.add_dependency(build_first, build_second)

	return graph


def order_projects(projects_list):
	# Return a list of the projects in a correct build order.
	build_order = []
	num_of_projects = len(projects_list)

	while len(build_order) < num_of_projects:
		to_be_processed = []

		# Figure out which projects can be built.
		for project in projects_list:
			if project.get_num_dependencies() == 0:
				to_be_processed.append(project)

		# Circular dependency: no remaining projects with zero dependencies.
		if len(to_be_processed) == 0:
			return None

		# Update dependency counts of children projects.
		for completed_project in to_be_processed:
			update_these_children = completed_project.get_children()
			for project in update_these_children:
				project.decrement_dependencies()

			# Update projects_list.
			projects_list.remove(completed_project)

		# Update build_order.
		build_order.extend(to_be_processed)

	return build_order









