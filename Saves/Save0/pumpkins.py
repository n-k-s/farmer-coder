clear()
start_time = get_time()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()): 
			if (get_time() - start_time) > 120:
				harvest()
				start_time = get_time()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)