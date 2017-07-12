"""
You are given a list of projects and list of dependencies (which is a
list of pairs of projects, where the second project is dependent on the
first project). All of a project's dependencies must be built before
the project is. Find a build order that will allow the projects to be
built. If there is no valid build order, return an error.
"""


class Node():
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		left = None
		right = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data

		return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def find_build_order(projects, dependencies):
	dependencies_dict = {}

	for dependency in dependencies:
		build_first, build_second = (dependency)

		if build_second not in dependencies_dict:
			dependencies_dict[build_second] = [build_first]
		else:
			dependencies_dict[build_second].append(build_first)


	build_order = []

	for project in projects:
		if project not in dependencies_dict.keys():
			build_order.append(project)
	
	if len(build_order) == 0:
		return None
	else:
		return build_order


# Testing
# pairs: second project is dependent on the first project
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]


# Expected result: f, e, a, b, d, c
build_order = find_build_order(projects, dependencies)
print(build_order)



