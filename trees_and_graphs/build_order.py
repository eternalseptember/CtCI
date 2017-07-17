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


def find_build_order(projects_list, dependencies_list):
	dependencies = {}
	build_order = []

	# organize dependencies
	for dependency in dependencies_list:
		build_first, build_second = (dependency)

		if build_second not in dependencies:
			dependencies[build_second] = [build_first]
		else:
			dependencies[build_second].append(build_first)

	# projects with no prerequisites
	for project in projects:
		if project not in dependencies.keys():
			build_order.append(project)

	# projects with prerequisites
	new_project_built = True

	while new_project_built:
		newly_added = []

		for project in dependencies.keys():
			project_dependencies = dependencies[project]

			meets_all_requirements = True
			for project_requirement in project_dependencies:
				if project_requirement not in build_order:
					meets_all_requirements = False
					break

			if meets_all_requirements:
				build_order.append(project)
				newly_added.append(project)


		if len(newly_added) > 0:
			# remove newly added projects from the pending projects list
			for project in newly_added:
				del dependencies[project]
		else:
			# no project was newly added
			new_project_built = False


	if len(build_order) < len(projects):
		return None
	else:
		return build_order


# Test Case 1
# pairs: second project is dependent on the first project
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

# Expected result: f, e, a, b, d, c
build_order = find_build_order(projects, dependencies)
print(build_order)


# Test Case 2
projects = ['a', 'b', 'c', 'd', 'e']
dependencies = [('c','a'), ('e','b'), ('b','a'), ('d','e'), ('b','d')]

# Expected result: None
build_order = find_build_order(projects, dependencies)
print(build_order)


# Test Case 3
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
dependencies = [('i','e'), ('d','c'), ('f','d'), ('c','a'), ('g','e'), ('d','b'), ('h','b'), ('e','c'), ('b','g')]

# Expected result: 
build_order = find_build_order(projects, dependencies)
print(build_order)


# Test Case 4
projects = ['a', 'b', 'c']
dependencies = [('a','b'), ('b','a')]

# Expected result: None
build_order = find_build_order(projects, dependencies)
print(build_order)


