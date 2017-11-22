"""
Implementing the second solution in the answer key.
Also called a topological sort algorithm.

O(P+D) time, where P is the number of projects and D is the number
of dependency pairs.

DFS version.
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
        self.state = 'blank'

    def add_edge(self, new_node):
        if new_node.name not in self.node_map:
            self.children.append(new_node)
            self.node_map[new_node.name] = new_node
            new_node.increment_dependencies()

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

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
    stack = []

    for project in projects_list:
        if (project.get_state() == 'blank'):
            if not do_DFS(project, stack):
                return None

    return stack


def do_DFS(project, project_stack):
    if (project.get_state() == 'partial'):
        return False  # Cycle

    if (project.get_state() == 'blank'):
        project.set_state('partial')

        children = project.get_children()
        for child_project in children:
            if not do_DFS(child_project, project_stack):
                return False

        project.set_state('complete')
        project_stack.push(project)

    return True











