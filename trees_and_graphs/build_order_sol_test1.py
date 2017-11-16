"""
Testing the provided solution for the build order problem.

Plan:
1.) Refine 'Project' object.
** currently here **
2.) Test order_projects(graph.get_projects()).
    This also tests add_non_dependent(project_order, projects_list, offset).
3.) If build_graph and order_projects functions work, then
    find_build_order(projects_list, dependencies_list) should also work.
"""


from build_order_sol import *


def print_graph_details(comments, graph_object):
    print('\t\t{0}'.format(comments))
    print(graph_object)

    print('\n\nEach project object\'s details:')
    for node in graph1.get_projects():
        node.print_project_details()

    print('\n\n\n')


# Use these lists to test build_graph().
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies = [('d', 'g'), ('a', 'e'), ('b', 'e'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('b', 'a'), ('f', 'a')]


# Testing build_graph function.
graph1 = build_graph(projects, dependencies)

comments = 'Testing build_graph function.'
print_graph_details(comments, graph1)








