import math


# for new_point, check whether another point exists on the line from your_position to the new_point
# solutions detail - used to store information about the point
# which can be used later (distance from your_position and whether the point is a guard or a captain)
# distance - max distance that a shot can travel
# type - whether the point is a guard or a captain
def check_point(new_point, solutions_detail, solutions_lookup, distance, type, your_position):
    new_point = coordinate_transform(new_point, your_position)
    if new_point == [0, 0]:
        pass
    else:
        m = gradient(new_point)
        quad = find_quadrant(new_point)
        my_distance = get_distance(new_point)

        if my_distance <= distance:
            if (m, quad) in solutions_lookup:
                if my_distance < solutions_detail[str(m) + ' ' + str(quad)][0]:
                    solutions_detail[str(m) + ' ' + str(quad)] = \
                        [my_distance, type, int(new_point[0]), int(new_point[1]), quad]
            else:
                solutions_lookup.add((m, quad))
                solutions_detail[str(m) + ' ' + str(quad)] = \
                    [my_distance, type, int(new_point[0]), int(new_point[1]), quad]


# function to find which quadrant of the overall solution space a point is in
def find_quadrant(point):
    if point[0] >= 0 and point[1] >= 0:
        return 1
    elif point[0] < 0 and point[1] > 0:
        return 2
    elif point[0] < 0 and point[1] < 0:
        return 3
    elif point[0] > 0 and point[1] < 0:
        return 4
    else:
        return 0


# function to find the gradient of a line, assuming it passes through 0, 0
def gradient(point):
    if point[0] == 0:
        m = float('inf')
    else:
        m = point[1]/float(point[0])
    return m


# transform coordinate to a new coordinate system, centred around new_origin
def coordinate_transform(coordinate, new_origin):
    return [coordinate[0]-new_origin[0], coordinate[1]-new_origin[1]]


# calculate straight line distance between 0, 0 and vector
def get_distance(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)


# core function - the problem of bouncing a shot off a wall has been reframed as a problem of
# shooting into adjacent mirrored rooms
def solution(dimensions, your_position, guard_position, distance):

    # check for disallowed inputs
    if not all(isinstance(x, int) for x in dimensions + your_position + guard_position) \
            or not isinstance(distance, int):
        return "Something is wrong with the inputs!"

    if not (1 < dimensions[0] <= 1250) or not (1 < dimensions[1] <= 1250) or not(1 < distance <= 10000)\
            or not(0 < your_position[0] < dimensions[0]) or not(0 < your_position[1] < dimensions[1])\
            or not(0 < guard_position[0] < dimensions[0]) or not(0 < guard_position[1] < dimensions[1])\
            or your_position == guard_position:
        return "Something is wrong with the inputs!"

    # calculate the maximum number of rooms that the shot can travel
    positive_rooms_x = (distance // dimensions[0]) + 1
    positive_rooms_y = (distance // dimensions[1]) + 1

    # transform coordinate system from bottom left of 1st room to centre of 1st room (global coordinates)
    centre = [dimensions[0]/2.0, dimensions[1]/2.0]
    your_position = coordinate_transform(your_position, centre)
    guard_position = coordinate_transform(guard_position, centre)

    # initialise set and dict for tracking solutions
    # a set is used to look up points based on gradient and quadrant for speed
    # a dict is then used to store information about the point that can be used to
    # check if a point is closer than a previous point on the same line, or a point is a guard or a captain
    solutions_lookup = set()
    solutions_detail = {}

    # set up transforms that will mirror points in the 4 quadrants
    quad_transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]  # transforms for quad 1, 2, 3, 4
    centre_quad_transforms = [[1, 1]]  # transform used only for the 1st room
    i0_quad_transforms = [[1, 1], [1, -1]]  # transform for rooms directly above/below the centre room
    j0_quad_transforms = [[1, 1], [-1, 1]]  # transform for rooms directly right/left the centre room

    # initialise working points
    local_centre = [0, 0]
    local_you = [0, 0]
    local_guard = [0, 0]

    # this loop does the work
    # loop over x rooms, y rooms and the mirrored rooms for each
    for i in range(positive_rooms_x+1):
        for j in range(positive_rooms_y+1):

            if i == 0 and j == 0:
                transforms = centre_quad_transforms
            elif i == 0:
                transforms = i0_quad_transforms
            elif j == 0:
                transforms = j0_quad_transforms
            else:
                transforms = quad_transforms

            for t in transforms:

                # find the centre of the current room in the global coordinates
                local_centre[0] = (i * dimensions[0]) * t[0]
                local_centre[1] = (j * dimensions[1]) * t[1]

                # mirror x position in global coordinates
                if i % 2 == 0:
                    local_guard[0] = local_centre[0] + guard_position[0]
                    local_you[0] = local_centre[0] + your_position[0]
                else:
                    local_guard[0] = local_centre[0] - guard_position[0]
                    local_you[0] = local_centre[0] - your_position[0]

                # mirror y position in global coordinates
                if j % 2 == 0:
                    local_guard[1] = local_centre[1] + guard_position[1]
                    local_you[1] = local_centre[1] + your_position[1]
                else:
                    local_guard[1] = local_centre[1] - guard_position[1]
                    local_you[1] = local_centre[1] - your_position[1]

                # check whether the new guard/captain is blocked by or blocks another instance of a guard/captain
                check_point(local_guard, solutions_detail, solutions_lookup, distance, 'guard',
                            your_position)
                check_point(local_you, solutions_detail, solutions_lookup, distance, 'you',
                            your_position)

    # for all points that can be hit by you, only guards are added to the number of possible directions
    directions = 0
    for k, v in solutions_detail.iteritems():
        if v[1] == 'guard':
            directions += 1

    return directions


if __name__ == '__main__':
    x1, y1, z1, w1 = [3,2], [1,1], [2,1], 4
    print 'solution 1 (7):', solution(x1, y1, z1, w1)
    x1, y1, z1, w1 = [300,275], [150,150], [185,100], 500
    print 'solution 2 (9):', solution(x1, y1, z1, w1)
    x1, y1, z1, w1 = [10, 10], [4, 4], [3, 3], 5000
    print 'solution 3 (739323):', solution(x1, y1, z1, w1)
    x1, y1, z1, w1 = [23, 10], [6, 4], [3, 2], 23
    print 'solution 4 (8):', solution(x1, y1, z1, w1)
    x1, y1, z1, w1 = [2, 5], [1, 2], [1, 4], 11
    print 'solution 5 (27):', solution(x1, y1, z1, w1)
    x1, y1, z1, w1 = [10, 10], [1, 1], [7, 9], 10
    print 'solution 6 (1):', solution(x1, y1, z1, w1)
    print 'solution 7 (167):', solution([846, 1087], [670, 339], [210, 88], 6995)
    #print 'solution 8 (??):', solution([8, 10], [1, 6], [6, 7], 7)
