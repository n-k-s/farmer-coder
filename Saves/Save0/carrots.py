from home_kit import *
clear()
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			move(North)
	move(East)	