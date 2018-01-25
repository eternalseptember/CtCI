"""
You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random
node from the tree. All nodes should be equally likely to be chosen. Design
and implement an algorithm for getRandomNode, and explain how you would
implement the rest of the methods.
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


def insert(head, data):
    if head is None:
        return Node(data)

    queue = [head]

    while len(queue) > 0:
        single_node = queue.pop(0)

        if single_node.left is not None:
            queue.append(single_node.left)
        else:
            single_node.left = Node(data)
            return head

        if single_node.right is not None:
            queue.append(single_node.right)
        else:
            single_node.right = Node(data)
            return head


def find(head, target):
    # find a node based on values
    queue = [(None, head)]

    while len(queue) > 0:
        top_of_stack = queue.pop(0)
        parent_node, current_node = (top_of_stack)

        left_match = False
        right_match = False

        if (current_node.left is None) and (target.left is None):
            left_match = True
        elif (current_node.left is not None) and (target.left is not None):
            if (current_node.left.data == target.left.data):
                left_match = True

        if (current_node.right is None) and (target.right is None):
            right_match = True
        elif (current_node.right is not None) and (target.right is not None):
            if (current_node.right.data == target.right.data):
                right_match = True


        if (current_node.data == target.data) and (left_match is True) and (right_match is True):
            return True, current_node, parent_node
        else:
            if current_node.left is not None:
                queue.append((current_node, current_node.left))
            if current_node.right is not None:
                queue.append((current_node, current_node.right))


    return False, None, None


def delete(head, target):
    # remove the first node with matching head data, left data, and right data
    # return True if node has been deleted
    # return False if node cannot be deleted
    node_found, found_head, parent_head = find(head, target)

    if node_found is True:
        # check content of nodes
        print('parent head: {0}'.format(parent_head))
        print('found head: {0}'.format(found_head))


        # delete policy: move the lower value upward

        # if the node to be deleted is the head
        if parent_head == found_head:
            match = 'head'
        # otherwise, figure out which child of parent_head to update
        elif parent_head.left == found_head:
            match = 'left'
        else:
            match = 'right'

        # figure out which child node moves upward
        if (found_head.left is None) and (found_head.right is None):
            move_up_child = 'none'
        elif (found_head.left is None):
            move_up_child = 'right'
        elif (found_head.right is None):
            move_up_child = 'left'
        else:
            if found_head.left.data <= found_head.right.data:
                move_up_child = 'left'
            else:
                move_up_child = 'right'


        # I don't think this is quite right...
        # it might need to keep moving values until it reaches a leaf node
        if match == 'left':
            if move_up_child == 'left':
                parent_head.left = found_head.left
            elif move_up_child == 'right':
                parent_head.left = found_head.right
            else:
                parent_head.left = None
        else:
            if move_up_child == 'left':
                parent_head.right = found_head.left
            elif move_up_child == 'right':
                parent_head.right = found_head.right
            else:
                parent_head.right = None



        return head
    else:
        return None



def get_random_node(head):
    from random import randrange

    list_of_nodes = []

    # fill list here
    queue = [head]
    while (len(queue) > 0):
        top_node = queue.pop(0)
        list_of_nodes.append(top_node)

        if top_node.left is not None:
            queue.append(top_node.left)
        if top_node.right is not None:
            queue.append(top_node.right)

    # get random node
    number_of_nodes = len(list_of_nodes)
    random_node_index = randrange(number_of_nodes)
    return list_of_nodes[random_node_index]





