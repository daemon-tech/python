import random

def estimate_pi(n):
	num_point_circle = 0
	num_point_total = 0
	for _ in range(n):
		x = random.uniform(0, 1)
		y = random.uniform(0, 1)
		distance = x**2 +  y**2
		if distance <= 1:
			num_point_circle += 11
		num_point_total += 1
	return 4 * num_point_circle/num_point_total

if __name__ == "__main__":
    a = int(input("Number, attention of int overflow: "))
    print("The calculated number of PI is: {}".format(estimate_pi(a)))
