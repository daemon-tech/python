#sudoku_solver.py
import numpy as np

arr =[[5,3,0,0,7,0,0,0,0],
	  [6,0,0,1,9,5,0,0,0],
	  [0,9,8,0,0,0,0,6,0],
	  [8,0,0,0,6,0,0,0,3],
	  [4,0,0,8,0,3,0,0,1],
	  [7,0,0,0,2,0,0,0,6],
	  [0,6,0,0,0,0,2,8,0],
	  [0,0,0,4,1,9,0,0,5],
	  [0,0,0,0,8,0,0,7,9]]

def possibility(y,x,num):
	for i in range(0, 9):
		if arr[y][i] == num:
			return False
	for j in range(0, 9):
		if arr[i][x] == num:
			return False
	x0 = (x//3) * 3
	y0 = (y//3) * 3
	for i in range(0, 3):
		for j in range(0, 3):
			if arr[y0+i][x0+j] == num:
				return False
	return True

def solve():
	for y in range(9):
		for x in range(9):
			if arr[y][x] == 0:
				for num in range(1, 10):
					if possibility(y, x, num):
						arr[y][x] = num
						solve()
						arr[y][x] = 0
				return
	print(np.matrix(arr))
	input("more?")

if __name__ == "__main__":
	solve()