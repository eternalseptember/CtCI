# Testing original solution to paths with sum problem.


from paths_with_sum import *
# from paths_with_sum_sol_1 import *
# from paths_with_sum_sol_2 import *


# Binary Tree 1
node_a = Node(-1)
node_b = Node(5)
node_c = Node(-11)
node_d = Node(4)
node_e = Node(2, None, node_a)
node_f = Node(6, node_b, node_c)
node_g = Node(9, node_d)
node_h = Node(7, node_e, node_f)
node_i = Node(5, None, node_g)
node_j = Node(-2, node_h, node_i)

# Expected result: 2
total_sum = 16
num_of_paths = count_paths(node_j, total_sum)
print(num_of_paths)


# Binary Tree 2
node_a = Node(3)
node_b = Node(-2)
node_c = Node(1, node_a, node_b)
node_d = Node(4)
node_e = Node(2, node_c, node_d)
node_f = Node(5)
node_g = Node(-4, node_f)
node_h = Node(1)
node_i = Node(1, node_h, node_g)
node_j = Node(3)
node_k = Node(-1, None, node_j)
node_l = Node(4, node_k, node_i)
node_m = Node(-3, node_e, node_l)
node_n = Node(10)
node_o = Node(-10, None, node_n)
node_r = Node(-10)
node_s = Node(10, node_r)
node_p = Node(3, node_s, node_o)
node_q = Node(7, node_m, node_p)

# Expected result: 10
total_sum = 10
num_of_paths = count_paths(node_q, total_sum)
print(num_of_paths)


# Binary Tree 3
node_a = Node(0)
node_b = Node(3, None, node_a)
node_c = Node(4, node_b)
node_d = Node(2)
node_e = Node(-1, node_d, node_c)

# Expected result: 1
total_sum = 0
num_of_paths = count_paths(node_e, total_sum)
print(num_of_paths)


# Binary Tree 4
node_a = Node(1)

# Expected result: 0
total_sum = 10
num_of_paths = count_paths(node_a, total_sum)
print(num_of_paths)



# Binary Tree 5
node_a = Node(4)
node_b = Node(4)
node_c = Node(4, node_a, node_b)

# Expected result: 3
total_sum = 4
num_of_paths = count_paths(node_c, total_sum)
print(num_of_paths)



# Binary Tree 6
node_a = Node(2)
node_b = Node(-2, None, node_a)
node_c = Node(-2)
node_d = Node(0)
node_e = Node(2, node_c, node_d)
node_f = Node(0, node_b, node_e)


# Expected result: 6
total_sum = 0
num_of_paths = count_paths(node_f, total_sum)
print(num_of_paths)


print()
# Binary Tree from the solution
node_a = Node(3)
node_b = Node(-2)
node_c = Node(3, node_a, node_b)
node_d = Node(1)
node_e = Node(2, None, node_d)
node_f = Node(5, node_c, node_e)
node_g = Node(11)
node_h = Node(-3, None, node_g)
node_i = Node(10, node_f, node_h)

# Expected result: 3
total_sum = 8
num_of_paths = count_paths(node_i, total_sum)
print(num_of_paths)






