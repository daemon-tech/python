import numpy as np
#list_comprehension.py
#18x7

grid_max_value = 18*7
grid = [i+1 for i in range(0, grid_max_value+1)]
print(grid)

for i in range(0, 9+1):
	for j in range(0, 15+1):
		grid.pop([j])


print(grid)
