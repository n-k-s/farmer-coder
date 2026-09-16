def move_to(x_goal: int, y_goal: int):
	while get_pos_x() != x_goal or get_pos_y() != y_goal:

		x, y = get_pos_x(), get_pos_y()
		if x < x_goal:
			move(East)
		if x > x_goal:
			move(West)
		if y < y_goal:
			move(North)
		if y > y_goal:
			move(South)
	return True


def fill_list(size: int):
	result = []
	for i in range(size):
		for j in range(size):
			result.append((i, j))
	return result
