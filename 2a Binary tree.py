def get_parent(x, h):
    root = 2 ** h - 1   # find root number = number of nodes in the tree

    if root <= x:       # if number being searched for is the root of the tree or higher
        return -1
    else:
        w = True
        sol = -1        # default solution
        offset = 0      # initialise offset, assuming starting at the root node
        subtree_size = root  # start at the root node
        while w:
            if subtree_size == 0:
                w = False

            subtree_size = subtree_size//2          # calculate new subtree size - this shorthand for (n-1)/2
            left_node = subtree_size + offset
            right_node = left_node + subtree_size
            curr_node = right_node + 1

            if (left_node == x) or (right_node == x):
                sol = curr_node
                w = False

            if x > left_node:                      # check if we need to search in the right node
                offset = left_node                 # if in the right node, adjust offset to account for the numbers in the left node

    return sol


def solution(height, to_check):
    return [get_parent(i, height) for i in to_check]


if __name__ == '__main__':
    h = 30
    q = [19, 14, 28]
    print(solution(h, q))
