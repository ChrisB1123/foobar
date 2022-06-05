from math import sqrt


def answer(dimensions, captain_position, badguy_position, distance):
    # deal with edge cases
    if dimensions[0] <= 1 or dimensions[0] > 1000:
        return 0
    if dimensions[1] <= 1 or dimensions[1] > 1000:
        return 0
    if distance <= 1 or distance > 1000:
        return 0

    count = 0
    for x in range(-dimensions[0], dimensions[0]):
        for y in range(-dimensions[0], dimensions[1]):
            current_laser_position = captain_position
            current_distance = 0
            new_bearing = [x, y]

            while (True):
                end_position = get_end_position(current_laser_position, new_bearing)
                wasBadGuyHit = check_if_hit_coordinate(current_laser_position, end_position, badguy_position)
                wasCaptainHit = check_if_hit_coordinate(current_laser_position, end_position, captain_position)

                if wasCaptainHit:
                    break

                if wasBadGuyHit:
                    current_distance += get_distance(start_position, badguy_position)
                    if current_distance > distance:
                        break
                    else:
                        count += 1
                        break

                current_distance += get_distance(start_position, end_position)
                if current_distance > distance:
                    break
                new_bearing = get_next_bearing(new_bearing, current_laser_position, end_position)
                current_laser_position = end_position

    return 0


def get_closest_wall(bearing, dimensions):
    if bearing[0] == 0 and bearing[1] > 0:
        return 0
    if bearing[0] == 0 and bearing[1] < 0:
        return 2
    if bearing[1] == 0 and bearing[0] > 0:
        return 1
    if bearing[1] == 0 and bearing[0] < 0:
        return 3

    if bearing[0] > 0 and bearing[1] > 0:
        return 2


def get_next_bearing(current_bearing, current_laser_position, end_position, wall_number):
    new_bearing = [0, 0]
    if current_bearing[0] > 0 and current_bearing[1] > 0:
        if wall_number == 0:
            new_bearing[0] = end_position[0] + current_bearing[0]
            new_bearing[1] = end_position[1] - current_bearing[1]
        if wall_number == 1:
            new_bearing[0] = end_position[0] - current_bearing[0]
            new_bearing[1] = end_position[1] + current_bearing[1]

    if current_bearing[0] < 0 and current_bearing[1] > 0:
        if wall_number == 0:
            new_bearing[0] = end_position[0] + current_bearing[0]
            new_bearing[1] = end_position[1] - current_bearing[1]
        if wall_number == 3:
            new_bearing[0] = end_position[0] - current_bearing[0]
            new_bearing[1] = end_position[1] + current_bearing[1]

    if current_bearing[0] < 0 and current_bearing[1] < 0:
        if wall_number == 3:
            new_bearing[0] = end_position[0] - current_bearing[0]
            new_bearing[1] = end_position[1] + current_bearing[1]
        if wall_number == 2:
            new_bearing[0] = end_position[0] + current_bearing[0]
            new_bearing[1] = end_position[0] - current_bearing[1]

    if current_bearing[0] > 0 and current_bearing[1] < 0:
        if wall_number == 2:
            new_bearing[0] = end_position[0] + current_bearing[0]
            new_bearing[1] = end_position[1] - current_bearing[1]
        if wall_number == 1:
            new_bearing[0] = end_position[0] - current_bearing[0]
            new_bearing[1] = end_position[0] + current_bearing[1]
    return new_bearing


def get_distance(start_position, end_position):
    x = abs(start_position[0] - end_position[0])
    y = abs(start_position[1] - end_position[1])
    return sqrt(pow(x, 2) + pow(y, 2))


def get_end_position(start_position, bearing):
    return


def check_if_hit_coordinate(start, end, position):
    return True


dimensions = [3, 2]
captain_position = [1, 1]
badguy_position = [2, 1]
distance = 4
print answer(dimensions, captain_position, badguy_position, distance)