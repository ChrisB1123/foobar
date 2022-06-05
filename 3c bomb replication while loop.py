# function to create children based on the possible replication rules
def children(parent):

    # left child
    m_new = parent['m']
    f_new = parent['f'] + parent['m']

    # id initialised as 0 and is assigned in the main loop
    left_node = {'id': 0, 'gen': parent['gen']+1, 'm': m_new, 'f': f_new}

    # right child
    m_new = parent['m'] + parent['f']
    f_new = parent['f']

    # id initialised as 0 and is assigned in the main loop
    right_node = {'id': 0, 'gen': parent['gen']+1, 'm': m_new, 'f': f_new}

    return left_node, right_node


def solution(m, f):
    search_m = long(m)
    search_f = long(f)
    unvisited_nodes = {}
    # dict to store solutions, based on the assumption it's possible there may be multiple nodes that meet the criteria
    solutions = {}

    if search_m == 1:
        return search_f + 1
    elif search_f == 1:
        return search_m + 1
    elif abs(search_m - search_f) == 1:
        return min(search_m, search_f)
    else:
        # define node as a dict containing the node's ID, the generation that the node is on and the number of m/f bombs
        root = {'id': 1, 'gen': 0, 'm': 1, 'f': 1}
        unvisited_nodes[1] = root

        w = True
        current_node = root
        id_counter = 2
        while w:

            # generate children
            left, right = children(current_node)

            # assign ids, used to reference nodes in the unvisited_nodes dictionary
            left['id'] = id_counter
            id_counter += 1
            right['id'] = id_counter
            id_counter += 1

            # if left child is the solution, store it the number of generations
            # else if the number of makes mean this child is no feasible then ignore it,
            # else store it to visit later
            if left['m'] == search_m and left['f'] == search_f:
                solutions[current_node['id']] = current_node['gen']+1
            elif left['m'] > search_m or left['f'] > search_f:
                pass
            elif left['m'] + left['f'] > search_m + search_f:
                pass
            else:
                unvisited_nodes[left['id']] = left

            # if right child is the solution, store it the number of generations
            # else if the number of makes mean this child is no feasible then ignore it,
            # else store it to visit later
            if right['m'] == search_m and right['f'] == search_f:
                solutions[current_node['id']] = current_node['gen']+1
            elif right['m'] > search_m or right['f'] > search_f:
                pass
            elif right['m'] + right['f'] > search_m + search_f:
                pass
            else:
                unvisited_nodes[right['id']] = right

            # delete the node that has now been visited
            unvisited_nodes.pop(current_node['id'])

            # once all nodes have been visited, break from loop, else get the next node
            if not unvisited_nodes:
                w = False
            else:
                current_node = unvisited_nodes.itervalues().next()

        # if no solution found, impossible, else find the solution with the minimum number of generations
        if not solutions:
            return "impossible"
        else:
            min_generations = float('inf')
            for key, value in solutions.iteritems():
                min_generations = min(min_generations, value)

            return str(min_generations)


if __name__ == '__main__':
    print 'test 1 output:', solution('2000', '2001')
    print 'test 2 output:', solution('4', '3')