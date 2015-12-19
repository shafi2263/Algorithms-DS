#
#A simple representation of Heapsort using min-heap property
#Heaps are almost-complete binary tree which must produce O(lg n) levels

#-- min_heapify maintains the max heap property of a heap and takes O(lg n) as it performs 
#-- only constant operations in each levels i.e. comapring parent with its child and if 
#-- necessary swap parent with it the larger one of its child

def min_heapify(arr, i, n):
	left = i*2+1
	right = i*2+2
	smallest = i

	if left <= n and arr[left]  < arr[i]:
		smallest = left

	if right <= n and arr[right] < arr[smallest]:
		smallest = right

	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		min_heapify(arr, smallest, n)
	

#build_min_heap builds up a heap with min_heap property it tightly takes linear time O(n)
#-- each n/2+1 and n/2+2 element of an array is a leaf which is the root of a min-heap
#
def build_min_heap(arr, n):
	i = n//2
	while (i >=0):
		min_heapify(arr,i, n)
		i -= 1


#heapsort sorts an array in desceding order using the min_heap property takes O(n lg n) time
def heapsort(arr, n):
	build_min_heap(arr, n)

	i = n
	while(i>=1):
		arr[0], arr[i] = arr[i], arr[0]
		min_heapify(arr, 0, i-1)
		i -= 1


if __name__=='__main__':
	arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	heapsort(arr, len(arr)-1)
	print(arr)