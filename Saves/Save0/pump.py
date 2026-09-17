from utils import *

size = get_world_size()

for x in range(size):
	col = range(size) if x % 2 == 0 else range(size - 1, -1, -1)
	for y in col:
		move_to(x, y)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)

while True:
	harvest()
	move_to(0, 0)
