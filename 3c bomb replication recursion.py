# define a recursive class which will keep creating children until the children's number of bombs
# are greater than the number of bombs that we are searching for
class Node:

    def __init__(self, gen, my_mach, my_facula):
        self.generation = gen
        self.bombs = {'m': my_mach, 'f': my_facula}

        # if current nodes children are the exact amount of bombs being searched for,
        # update the global variable, else continue creating children
        if my_mach == search_m and my_facula == search_f:
            global min_generations
            min_generations = min(min_generations, gen)
        else:
            # recursive method call - children are created as new nodes
            self.children()

    def children(self):

        # left child
        m_new = self.bombs['m']
        f_new = self.bombs['f'] + self.bombs['m']

        # check if children's bombs are larger than what we are searching for,
        # if so, then crease creating children
        if m_new > search_m or f_new > search_f:
            left_node = None
        else:
            left_node = Node(self.generation+1, m_new, f_new)

        # right child
        m_new = self.bombs['m'] + self.bombs['f']
        f_new = self.bombs['f']

        # check if children's bombs are larger than what we are searching for,
        # if so, then crease creating children
        if m_new > search_m or f_new > search_f:
            right_node = None
        else:
            right_node = Node(self.generation+1, m_new, f_new)

def solution(m, f):
    # set global variables to be referenced against/updated during recursion
    global search_m
    global search_f
    global min_generations

    search_m = long(m)
    search_f = long(f)
    min_generations = float('inf')

    # define root node
    Node(0, 1, 1)

    if min_generations == float('inf'):
        return "impossible"
    else:
        return str(min_generations)


if __name__ == '__main__':
    print 'test 1 output:', solution('2', '1')
    print 'test 2 output:', solution('4', '7')
