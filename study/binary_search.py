def sorting(elements):

	for i in range(len(elements)):
		for j in range(len(elements)):
			if elements[i] < elements[j]:
				value_j = elements[j]
				elements[j] = elements[i]
				elements[i] = value_j
	for i in range(len(elements)):
		if i != len(elements) - 1:
			print(elements[i], end=", ")
		else:
			print(elements[i]) 

def binary_search(elements, n):
	first = 0
	last = len(elements)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if elements[mid] == n :
			found = True
		else:
			if n < elements[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	print(binary_search(elements, n))

if __name__ == "__main__":
	n = 44
	elements = [90, 84, 77, 44, 38, 23, 17, 12, 5]
	sorting(elements)
	binary_search(elements, n)
