#implementation of max_priority_queue using the max_heap property of heap
#insertion takes O(lg n) time while extraction of max element takes the same
from math import floor

class MaxPriorityQueue(object):

	def __init__(self):
		self.array = []

	
	def is_empty(self):
		return self.array == []

	
	def size(self):
		return len(self.array)

	
	def max_heapify(self, i):
		left = i*2+1
		right = i*2+2

		largest = i

		if left<self.size() and self.array[left] > self.array[i]:
			largest = left
		if right < self.size() and self.array[right] > self.array[largest]:
			largest = right

		if largest != i:
			self.array[i], self.array[largest] = self.array[largest], self.array[i]
			self.max_heapify(largest)




	def heap_increase_key(self, array, n, key):
		if key < array[n]:
			raise Exception("Key is smaller than the current key")
			return
		array[n] = key
		while n > 0 and array[floor((n-1)/2)] < array[n]:
			array[n], array[floor((n-1)/2)] = array[floor((n-1)/2)], array[n]
			n = floor((n-1)/2)


	def insert(self, key):
		n = len(self.array)
		self.array.append(-(2**64))
		self.heap_increase_key(self.array, n, key)

	
	def peek(self):
		if not self.is_empty():
			return self.array[0]
		else:
			raise Exception("Queue is empty")

	def pop(self):
		if not self.is_empty():
			maximum = self.array[0]
			del self.array[0]

			self.max_heapify(0)
			return maximum

		else:
			raise Exception("Queue is empty")


	def __repr__(self):
		return str(self.array)