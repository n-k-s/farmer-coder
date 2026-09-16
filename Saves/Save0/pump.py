from utils import move_to


size = get_world_size()
#TODO True nearest-neighbor traversal 
while True:
	for i in range(size):
		for j in range(size):
			move_to(i, j)
			if can_harvest():
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Pumpkin)
	harvest()
	move_to(0, 0)
