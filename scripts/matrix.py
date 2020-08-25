import time
import random

items = [chr(i) for i in range(0, 1+1)]

for i in range(0, 1+1): #spaces n numbers
	items.append(str(i*i))
for j in range(1, 10+1):
	items.append(" "*j)

def shower(row, column): #func for row, column
	for i in range (row):
		s = '' #new str
		for j in range(column):
			ri = random.randrange(len(items)) #rnd index
			s += items[ri]
		print(s)
		time.sleep(0.01) #shower speed

while True:
	shower(99, 99)
