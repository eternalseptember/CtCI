# Test cases for build-order problems.
# Pairs: second project is dependent on the first project

from build_order import *
# from build_order_sol_1 import *


# Test Case 1
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

# Expected result: f, e, a, b, d, c
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)



# Test Case 2
projects = ['a', 'b', 'c', 'd', 'e']
dependencies = [('c','a'), ('e','b'), ('b','a'), ('d','e'), ('b','d')]

# Expected result: None
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)



# Test Case 3
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
dependencies = [('i','e'), ('d','c'), ('f','d'), ('c','a'), ('g','e'), ('d','b'), ('h','b'), ('e','c'), ('b','g')]

# Expected result: a valid build order
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)



# Test Case 4
projects = ['a', 'b', 'c']
dependencies = [('a','b'), ('b','a')]

# Expected result: None
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)



# Test Case 5, from answer key
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies = [('d', 'g'), ('a', 'e'), ('b', 'e'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('b', 'a'), ('f', 'a')]

# Expected result: a valid build order
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)



# Test case 6: simple test case
projects = ['a', 'b', 'c', 'd']
dependencies = [('a', 'b'), ('c', 'd')]

# Expected result: a valid build order
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)


