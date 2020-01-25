"""
Question: Suppose you have a list of a million repeating nos.

You need top 100 elements in order of frequency.
"""

#Max
class BinaryMaxHeap:
	def __init__(self): 
		self.heapsize=0
		self.heap_array=[]

	def insert_element(self, element):
		self.heap_array.append(element)
		self.heapsize+=1
		print ("inserting", element, "-->", self.heap_array)
		#current_location=self.heapsize-1 #(indexed location)
		current_location=self.heapsize #(indexed location)
		self.percolate_up(element,current_location)

	def get_max_element(self):
		return self.heap_array[0]

	def delete_max(self):
		print ("before delete:", self.heap_array)
		self.heap_array[0]=self.heap_array[-1]
		self.heap_array=self.heap_array[0:-1]
		current_location=1
		if len(self.heap_array) > 0:
			element=self.heap_array[0]
			self.heapsize-=1
			self.percolate_down(element,current_location)
			print ("final after delete:", self.heap_array)


	def percolate_up(self,element,current_location):
		parent_location=int(current_location/2)
		if parent_location==0:
			return
		else:
		    parent_location= parent_location-1
		current_location=current_location-1
		print ("parent_index_location:",parent_location, "; current_location:",current_location)
		print ("parent->",self.heap_array[parent_location])
		if (self.heap_array[parent_location]< element):
			print ("need to replace")
			tmp=self.heap_array[parent_location]
			self.heap_array[parent_location]=element
			self.heap_array[current_location]=tmp

			print ("after replace",self.heap_array)
			current_location=parent_location
			self.percolate_up(element,current_location+1)
			print ("returning")
		else:
			print ("no more percolating")
			return 
		print ("Finished--->", self.heap_array)



	def percolate_down(self,element,current_location):
		left_child_location=(2*current_location)-1
		right_child_location=(2*current_location+1)-1
		
		current_location=current_location-1


		if left_child_location > self.heapsize-1 or right_child_location  >= self.heapsize-1:
			return



		if self.heap_array[right_child_location] > self.heap_array[left_child_location] :
			child_location=right_child_location
		else:
			child_location=left_child_location

		print ("child_location:",child_location, "; current_location:",current_location)



		if self.heap_array[current_location] < self.heap_array[child_location]:
			tmp=self.heap_array[child_location]
			self.heap_array[child_location]=element
			self.heap_array[current_location]=tmp
			print ("after replace",self.heap_array)
			current_location=child_location
			self.percolate_down(element,current_location+1)


	def get_heap(self):
		print (self.heap_array)


if __name__=="__main__":
	heap=BinaryMaxHeap()
	heap.insert_element(6)
	print ("-----------------")
	heap.insert_element(2)
	print ("-----------------")
	heap.insert_element(7)
	print ("-----------------")
	heap.insert_element(9)
	print ("-----------------")
	heap.insert_element(10)
	print ("-----------------")
	heap.insert_element(5)
	print ("-----------------")
	heap.insert_element(8)
	print ("-----------------")
	heap.insert_element(12)
	print ("-----------------")



	print ("Deleting begins")

	for i in range(0,heap.heapsize):
		print ("iteration--------",i)
		heap.delete_max()
	


		
