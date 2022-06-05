# function to find the parent based on the replication rules.
# due to the symmetry of the potential replication options, whether bombs are m or f is ignored
def get_parent(child_bombs1, child_bombs2):
    dif = abs(child_bombs1 - child_bombs2)
    parent_bombs1 = dif
    parent_bombs2 = max(child_bombs1, child_bombs2) - dif

    return min(parent_bombs1, parent_bombs2), max(parent_bombs1, parent_bombs2)


def solution(m, f):
    search_m = long(m)
    search_f = long(f)

    # eliminate trivial solutions
    if search_m == 1 or search_f == 1:
        return str(max(search_f, search_m) - 1)
    elif abs(search_m - search_f) == 1:
        return str(min(search_m, search_f))
    else:
        generations = 1
        w = True

        # due to symmetry of tree of possibilities, ignore whether bombs are m or f
        bombs_high = max(search_m, search_f)
        bombs_low = min(search_m, search_f)
        while w:

            dif = bombs_high - bombs_low
            if dif/bombs_low >= 1:
                bombs_high = bombs_high - (dif//bombs_low)*bombs_low
                generations = generations + dif//bombs_low

            bombs_low, bombs_high = get_parent(bombs_high, bombs_low)

            # once we are close to the edge of the tree, directly calculate how many more generations are left
            if bombs_low == 1:
                return str(generations + bombs_high - 1)
            elif bombs_high - bombs_low == 1:
                generations = str(generations + bombs_low)
                return str(generations)
            elif bombs_low <= 0 or bombs_high <= 0:
                return 'impossible'

            generations += 1


if __name__ == '__main__':
    x = 10**50
    y = 7
    a = solution(str(x), str(y))
    print a