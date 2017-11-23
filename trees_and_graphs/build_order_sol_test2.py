# Testing the provided solution for the build order problem.


from build_order_sol_2 import *


# Use these lists to test build_graph().
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies = [('d', 'g'), ('a', 'e'), ('b', 'e'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('b', 'a'), ('f', 'a')]


project_order = find_build_order(projects, dependencies)
print(project_order)









