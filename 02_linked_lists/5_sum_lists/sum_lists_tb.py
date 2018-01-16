# Test cases for the "sum lists" problem.


from sum_lists import *


math_problems = [
                (10, 52),   # 62	-> 2 6
                (99, 201),  # 300	-> 0 0 3
                (999, 1),   # 1000	-> 0 0 0 1
                (102, 899)  # 1001	-> 1 0 0 1
                ]

for problem in math_problems:
    value1, value2 = problem
    head1 = convert_to_linked_list(value1)
    head2 = convert_to_linked_list(value2)
    total = add_linked_list_nums(head1, head2)

    print('Total in linked list format: ', end=' ')
    print_linked_list(total)
    print()

