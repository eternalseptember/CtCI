# Test cases for build-order problems.

from build_order import *


# Test Case 1
# pairs: second project is dependent on the first project
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

# Expected result: 
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)


# Test Case 4
projects = ['a', 'b', 'c']
dependencies = [('a','b'), ('b','a')]

# Expected result: None
build_order_results = find_build_order(projects, dependencies)
print(build_order_results)






