"""
You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the
number of paths that sum to a given value. The path does not need to
start or end at the root or a leaf, but it must go downwards (traveling
only from parent nodes to child nodes).
"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def print_level_order(head):
    queue = [head]

    while len(queue) > 0:
        head_node = queue.pop(0)
        print(head_node)
        if head_node.left is not None:
            queue.append(head_node.left)
        if head_node.right is not None:
            queue.append(head_node.right)


def count_paths(head, value):
    # return number of paths that sum to a given value
    total_paths = 0
    paths_list = get_paths(head, paths_list=[])


    for path_num in range(len(paths_list)):
        current_path = paths_list[path_num]
        same_path = True
        total = 0


        # what if paths are different lengths?
        if path_num > 0:
            prev_path_num = path_num - 1
            prev_path_length = len(paths_list[prev_path_num])


        for node_num in range(len(current_path)):
            total += current_path[node_num].data

            # determines if the path is unique
            if path_num == 0:
                same_path = False
            else:
                if node_num >= prev_path_length:
                    same_path = False
                elif current_path[node_num].data != paths_list[prev_path_num][node_num].data:
                    same_path = False

            # count unique paths
            if (total == value) and (same_path is False):
                """
                for node_counter in range(0, node_num+1):
                    print(paths_list[path_num][node_counter])
                print()
                """

                total_paths += 1

    return total_paths


def get_paths(head, current_path=[], next_position=0, paths_list=[]):
    # truncates the current path when going back up in the tree
    if len(current_path) > next_position:
        current_path = current_path[:next_position]
    current_path.append(head)

    if (head.left is None) and (head.right is None):
        paths_list.append(current_path)
        #print('\n')
        return paths_list

    if (head.left is not None):
        paths_list = get_paths(head.left, current_path, next_position+1, paths_list)
    if (head.right is not None):
        paths_list = get_paths(head.right, current_path, next_position+1, paths_list)

    return paths_list



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

# Expected result: 8
total_sum = 10
num_of_paths = count_paths(node_q, total_sum)
print(num_of_paths)


# Binary Tree 3
node_a = Node(0)
node_b = Node(3, None, node_a)
node_c = Node(4, node_b)
node_d = Node(2)
node_e = Node(-1, node_d, node_c)

# Expected result: 0
total_sum = 0
num_of_paths = count_paths(node_e, total_sum)
print(num_of_paths)




