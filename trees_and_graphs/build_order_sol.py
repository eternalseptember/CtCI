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

    # not entirely sure these functions are necessary?
    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_num_dependencies(self):
        return self.dependencies

    # Print things.
    def __str__(self):
        return 'Project {0}'.format(self.name)

    def __repr__(self):
        return 'Project {0}'.format(self.name)

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




