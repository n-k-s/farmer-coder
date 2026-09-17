# def move_to(x_goal: int, y_goal: int):
# 	while get_pos_x() != x_goal or get_pos_y() != y_goal:
# 		#TODO increase traversal efficiency, when you go up at max height, you go back to 0.
# 		x, y = get_pos_x(), get_pos_y()
# 		if x < x_goal:
# 			move(East)
# 		if x > x_goal:
# 			move(West)
# 		if y < y_goal:
# 			move(North)
# 		if y > y_goal:
# 			move(South)
# 	return True


from math import integer


def fill_list(size: int):
    result = []
    for i in range(size):
        for j in range(size):
            result.append((i, j))
    return result

def move_to(x_goal, y_goal):
	size = get_world_size()
	x, y = get_pos_x(), get_pos_y()
	x_min_dist = min(abs(x_goal-x), abs(size + x - x_goal))
	if abs(x_goal - x) == x_min_dist:
		x_move_positive = x_goal - x >= 0
	else:
		x_move_positive = x_goal - x < 0
	while (x != x_goal):
		if (x_move_positive):
			move(East)
		else:
			move(West)
		x = get_pos_x()

	y_min_dist = min(abs(y_goal-y), abs(size + y - y_goal))
	if abs(y_goal - y) == y_min_dist:
		y_move_positive = y_goal - y >= 0
	else:
		y_move_positive = y_goal - y < 0
	while (y != y_goal):
		if (y_move_positive):
			move(North)
		else:
			move(South)
		y = get_pos_y()


def find_nearest_neighbor(grid_coords):
    # check in a list of grid coordintaes to find the nearest neighbor.
	go_to = 999999999
	min_dist = get_world_size()
	x, y = get_pos_x(), get_pos_y()
	for i in grid_coords:
		x_grid_coord, y_grid_coord = i[0], i[1]
		dist = abs(x-x_grid_coord) + abs(y - y_grid_coord)
		if (dist < min_dist):
			min_dist = dist
			go_to = i
	return go_to
