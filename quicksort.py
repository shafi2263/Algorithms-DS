#Quicksort takes avg n lg n time but in worst case O(n^2)

#partioning the array with respect to pivot element
#Here Lomuto partioning is used
def partition(arr, p, r):
	pivot = arr[r]

	i = p-1

	for j in range(p, r):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[r] = arr[r], arr[i+1]
	return i+1


def quicksort(arr, p, r):
	if p < r:
		q = partition(arr, p , r)
		quicksort(arr, p , q-1)
		quicksort(arr, q+1, r)


if __name__== "__main__":
	arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	quicksort(arr, 0, len(arr)-1)
	print (arr)