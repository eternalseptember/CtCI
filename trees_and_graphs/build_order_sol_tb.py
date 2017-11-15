# Testing the solution for the build order problem.


from build_order_sol import *


graph1 = Graph()
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for node in nodes:
    graph1.get_or_create_node(node)


print('\t\tgraph1 object after adding nodes:')
print(graph1)
print()



edges = [('d', 'g'), ('a', 'e'), ('b', 'e'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('b', 'a'), ('f', 'a')]

for edge in edges:
    node1, node2 = (edge)
    graph1.add_edge(node1, node2)


print('\t\tgraph1 object after adding edges')
print(graph1)

