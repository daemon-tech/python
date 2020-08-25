class Figure():
	col:int
	row:int

#constructor
def __init__(self, pos: str):
	if len(pos) != 2:
		raise ValueError('Invalid position')
	c = pos[0].lower()
	r = pos[1]
	if (not c in 'abcdefgh') or (not r in '12345678'):
		raise ValueError('Invalid position')
	self.col = 'abcdefgh'.find(c)
	self.row = '12345678'.find(r)

#giving back postion
def __str__(self):
	return Figure.position(self.col, self.row)

#test if valid position
@staticmethod
def position(col: int, row: int)->str:
	if row<0 or row>7 or col<0 or col>7:
		return ''
	return 'abcdefgh'[col] + '12345678'[row]