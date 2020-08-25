#python
#pyramid test script

def pyramid(j):
	for i in range(1, 10, 2):
		print(" "*j+(i*"*"))
	j = j-1

if __name__ == "__main__":
	pyramid(9)
