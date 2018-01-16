# Test cases for "route between nodes" problem.


from route_between_nodes import *


# Graph 1
node0 = Node('node0')
node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')

node0.routes = [node1, node2]
node1.routes = [node2]
node2.routes = [node0, node3]
node3.routes = [node3]

# test case 1: true
result = has_route_between_nodes(node1, node3)
print(result)

# test case 2: false
result = has_route_between_nodes(node3, node0)
print(result)
print()


# Graph 2
node0 = Node('node0')
node1 = Node('node1')
node2 = Node('node2')

node0.routes = [node1]
node1.routes = [node2]

# test case 3: false
result = has_route_between_nodes(node2, node1)
print(result)

# test case 4: false
result = has_route_between_nodes(node2, node0)
print(result)

# test case 5: false
result = has_route_between_nodes(node1, node0)
print(result)

# test case 6: true
# Answer key assumes this to be true even if there isn't
# a node pointing back to itself.
result = has_route_between_nodes(node0, node0)
print(result)

# test case 7: true
result = has_route_between_nodes(node0, node1)
print(result)

# test case 8: true
result = has_route_between_nodes(node0, node2)
print(result)

# test case 9: true
result = has_route_between_nodes(node1, node2)
print(result)
print()


# Graph 3
nodeA = Node('nodeA')
nodeB = Node('nodeB')
nodeC = Node('nodeC')
nodeD = Node('nodeD')

nodeA.routes = [nodeB, nodeD]
nodeB.routes = [nodeC]
nodeC.routes = [nodeA]

# test case 10: true
result = has_route_between_nodes(nodeA, nodeC)
print(result)

# test case 11: true
result = has_route_between_nodes(nodeB, nodeD)
print(result)

# test case 12: false
result = has_route_between_nodes(nodeD, nodeC)
print(result)
