import itertools


# for a given 2d list of edge_weights, return a list of edges, defined by [start, end, weight]
def edge_list(edge_weights):
    num_nodes = len(edge_weights)

    edges_list = []
    edges_count = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                pass
            else:
                l = [i, j, edge_weights[i][j]]
                edges_list.append(l)
            edges_count += 1

    return edges_list


# bellman ford algorithm to return minimum distances between nodes, and identify if a negative cycle exists
def bellman_ford(src, edge_weights):
    num_nodes = len(edge_weights)

    inf = float('inf')

    distances = [inf for vertex in range(num_nodes)]  # initialise distances

    distances[src] = 0  # set distance of start point (src) to 0
    vertices = [i for i in range(num_nodes)]  # create list of vertices in the grid

    edges = edge_list(edge_weights)

    # iteratively calculate distances to all other nodes in the graph
    for i in range(num_nodes-1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # check if a negative cycle exists
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return []

    return distances


def solution(times, time_limit):

    num_vertices = len(times)
    num_bunnies = num_vertices-2
    bunnies = range(1, num_bunnies+1)
    vertices = range(num_vertices)

    # get routes between all vertices with minimum cost
    minimum_times = [bellman_ford(i, times) for i in vertices]


    print minimum_times

    # if a negative cycle exists, it is possible to pick up all bunnies
    if not any(minimum_times):
        answer = [i - 1 for i in bunnies]
        return answer

    solutions = {}
    s_count = 1

    # for each different order of bunnies, attempt to pick up the bunnies and then go to the exit
    for i in itertools.permutations(bunnies):
        # for each different order of bunnies, attempt to pick up increasingly less bunnies
        # there is some duplication in the routes that are tested,
        # however the size of the defined problem doesn't not warrant the additional complexity required to optimise this
        for j in range(num_bunnies):
            route = list(i[:num_bunnies-j])

            # add in the start and end nodes
            route.insert(0, 0)
            route.append(num_vertices-1)

            # calculate cost of the defined route
            delta = 0
            for k in range(len(route)-1):
                start = route[k]
                end = route[k+1]
                delta = delta + minimum_times[start][end]

            # assess whether the defined route can be completed within the time limit and record the solution
            if time_limit - delta >= 0:
                solutions[s_count] = route
                s_count += 1

    # format answer before returning, in line with the defined question
    answer = []
    max_len = 0
    for k, v in solutions.iteritems():
        # remove start and end points
        v.pop()
        v.pop(0)

        # find the solution with the most bunnies. If there are multiple solutions of the same length,
        # only return the first solution.
        # By the order in which the permutations are sorted through,
        # this will be the solution with the minimum indexed bunnies
        if len(v) > max_len:
            max_len = len(v)
            answer = v

    # reindex the bunnies so their numbers in line with how they are defined in the question, and sort
    answer = [i - 1 for i in answer]
    answer.sort()

    return answer


if __name__ == '__main__':
    x = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    y = 1
    print 'solution 1:', solution(x, y)
    x = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    y = 3
    #print 'solution 2:', solution(x, y)
    x = [[0, 1, 1, 5, 6, 9, 4], [5, 0, 4, 5, 4, 8, 6], [3, 2, 0, 2, 8, 2, 1], [4, 10, 8, 0, 10, 1, 7], [6, 7, 5, 1, 0, 2, 3], [3, 7, 8, 10, 5, 0, 10], [9, 4, 3, 4, 10, 2, 0]]
    y = 10
    #print 'solution 3:', solution(x, y)
    x = [[0, 9, -1, 9, 9], [9, 0, 9, 9, 9], [-1, 9, 0, 9, 9], [9, 9, 9, 0, 9], [9, 9, 9, 9, 9]]
    y = 1
    #print 'solution 4:', solution(x, y)

