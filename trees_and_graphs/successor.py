"""
Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each node
has a link to its parent.
"""


class Node:
    def __init__(self, data=None, left=None, right=None, prev=None):
        self.data = data
        self.left = left
        self.right = right
        self.prev = prev

    def __str__(self):
        left = None
        right = None
        prev = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data
        if self.prev is not None:
            prev = self.prev.data

        d_str = '{0}'.format(self.data).rjust(4)
        l_str = '{0}'.format(left).rjust(4)
        r_str = '{0}'.format(right).rjust(4)
        p_str = '{0}'.format(prev).rjust(4)

        return 'data: {0}    left: {1}    right: {2}    prev: {3}'.format(d_str, l_str, r_str, p_str)


def print_tree(head):
    if head.left is not None:
        print_tree(head.left)
    print(head)
    if head.right is not None:
        print_tree(head.right)


"""
def find_next_node(head):
    if head.right is not None:
        next_node = head.right

        while next_node.left is not None:
            next_node = next_node.left

        return next_node

    else:
        # there's no right node
        if head.prev is None:
            # root node
            return None
        else:
            next_node = head.prev
            
            if next_node.left == head:
                # go up the tree
                return next_node
            else:
                # check if need to return the root
                # or no more successors
                current_node = next_node
                next_node = current_node.prev

                if next_node is None:
                    return None
                else:
                    while next_node.prev is not None:
                        if next_node.left == current_node:
                            return next_node

                        current_node = next_node
                        next_node = current_node.prev

                    # made it to the root
                    if next_node.left == current_node:
                        return next_node
                    else:
                        return None
"""


def find_next_node(head):
    if head is None:
        return None

    # Found right children -> return left-most node of right subtree
    if head.right is not None:
        return left_most_child(head.right)
    else:
        # some assignments
        
    return None


def left_most_child(head):
    if head is None:
        return None

    while head.left is not None:
        head = head.next

    return head






