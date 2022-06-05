# the minimum size of the left step is limited by the sum of consecutive numbers
# due to the fact that the shortest solution for each number of bricks, will be where the solution
# is as close as possible to consecutive steps only have a 1 brick difference
def find_min_left_step(n):
    for i in xrange(1, n+1):
        consecutive_sum = ((float(i)/2)*(i+1))
        if consecutive_sum >= n:
            return i


def solution(n):
    if n < 3:
        return "Looks like we don't have enough bricks to make a staircase!"
    elif n > 200:
        return "Looks like that's too many bricks!"
    else:
        solutions = {1: 0, 2: 0}  # initialise trivial solutions

        # for each number of bricks (i), this dict stores the number of combinations that exist for
        # each size of left step. The structure of this dict is {Number of bricks: {left step size: number of combos}}
        step_details = {1: {1: 0}, 2: {1: 0}}  # initialise trivial solutions

        # loops over each problem size up to n, to calculate the number of combinations for a given n,
        # using solutions from previous iterations
        for i in xrange(3, n+1):
            min_left_step = find_min_left_step(i)
            solutions[i] = 0  # initialise answer, to be added to on each step
            step_details[i] = {}

            # loop over each possible size of left most step, for a given number of bricks
            for left_step in xrange(i-1, min_left_step-1, -1):
                right_bricks = i - left_step

                # if there are more bricks in the left step than there are to the right, then the number of combos
                # to be added is equivalent to the solution at n = right_bricks.
                # +1 for the case where all right bricks are in 1 step
                if left_step > right_bricks:
                    combos = solutions[right_bricks] + 1
                    solutions[i] = solutions[i] + combos
                    step_details[i][left_step] = combos

                # else if combos to be added is equivalent to the solution at n = right_bricks.
                # there is no +1 because it's not possible to stack all the right bricks in 1 step,
                # because this would violate the rule of no 2 steps being the same height
                elif left_step == right_bricks:
                    combos = solutions[right_bricks]
                    solutions[i] = solutions[i] + combos
                    step_details[i][left_step] = combos

                # else, where right_bricks > left_step, use the solution at n = right_bricks, only including combos
                # which have a left step less than the left step of the current iteration
                else:
                    combos = 0
                    for key, value in step_details[right_bricks].iteritems():
                        if key < left_step:
                            combos = combos + value

                    solutions[i] = solutions[i] + combos
                    step_details[i][left_step] = combos

    return solutions[n]


if __name__ == '__main__':
    print(solution(8))
    #print('n = 3, output =', solution(3))
    #print('n = 200, output =', solution(200))