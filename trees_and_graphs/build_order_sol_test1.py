"""
Testing the provided solution for the build order problem.

Plan:
1.) Test 'Graph' and 'Project' objects.
2.) Test build_graph(projects_list, dependencies_list).
3.) Test order_projects(graph.get_nodes()).
    This also tests add_non_dependent(project_order, projects_list, offset).
4.) If build_graph and order_projects functions work, then
    find_build_order(projects_list, dependencies_list) should also work.

"""


from build_order_sol import *


def print_graph_details(comments, graph_object):
    print('\t\t{0}'.format(comments))
    print(graph_object)
    print('\n\nEach project object\'s details:')

    for node in graph1.get_nodes():
        node.print_project_details()

    print('\n\n\n')


# Use these lists to test build_graph().
projects_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies_list = [('d', 'g'), ('a', 'e'), ('b', 'e'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('b', 'a'), ('f', 'a')]


# Each 'project' is a node in the graph.
graph1 = Graph()

for project in projects_list:
    graph1.get_or_create_node(project)

comments = 'graph1 object after adding nodes:'
print_graph_details(comments, graph1)


# Each 'edge' establishes a dependency.
for edge in dependencies_list:
    node1, node2 = (edge)
    graph1.add_edge(node1, node2)

comments = 'graph1 object after adding edges:'
print_graph_details(comments, graph1)









