while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			do_plant = (get_pos_x() % 2 == get_pos_y() % 2)
			if do_plant:
				if get_entity_type() == Entities.Tree and can_harvest():
					harvest()
				plant(Entities.Tree)
			move(North)
		move(East)