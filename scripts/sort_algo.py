#sorting algorythm

def sorting(arr):

	print("Unsorted Array: ", end=" ")
	print(arr)
	
	for i in range(0, len(arr)):
		for j in range(0+i, len(arr)):
			if arr[i] > arr[j]:
				value_j = arr[j]
				arr[j] = arr[i]
				arr[i] = value_j
	
	print("Sorted Array: ", end=" ")
	
	for n in range(0, len(arr)):
		print(arr[n], end=" ")

if __name__ == "__main__":
	arr = [234, 23, 34, 45, 566, 67, 223, 3, 345, 999, 1, 23, 66]
	sorting(arr)

