"""
Question: Suppose you have a list of a million repeating nos.

You need top 100 elements in order of frequency.
"""

class Node:
	def __init__(self,key, value):
		self.key=key
		self.value=value
		



class BinaryMaxHeap:
	def __init__(self): #fixed size heap
		self.heapsize=0
		self.heap_array=[]

	def find_minimum_element_loc(self):
		min_loc_index=self.heapsize-1
		for index in range(0, len(self.heap_array)):
			if self.heap_array[index].value < self.heap_array[min_loc_index].value:
				min_loc_index=index
		return min_loc_index


	def insert_element(self, element):
		self.heap_array.append(element)
		self.heapsize+=1
		#print ("inserting", element.value, "-->")
		#for item in self.heap_array:
		#	print item.key, item.value
		#current_location=self.heapsize-1 #(indexed location)
		current_location=self.heapsize #(indexed location)
		self.percolate_up(element,current_location)

	def get_max_element(self):
		return self.heap_array[0]

	def delete_max(self):
		#print ("before delete:", self.heap_array)
		self.heap_array[0]=self.heap_array[-1]
		self.heap_array=self.heap_array[0:-1]
		current_location=1
		if len(self.heap_array) > 0:
			element=self.heap_array[0]
			self.heapsize-=1
			self.percolate_down(element,current_location)
			#print ("final after delete:", self.heap_array)


	def percolate_up(self,element,current_location):
		parent_location=int(current_location/2)
		if parent_location==0:
			return
		else:
		    parent_location= parent_location-1

		current_location=current_location-1
		#print ("parent_index_location:",parent_location, "; current_location:",current_location)
		#print ("parent->",self.heap_array[parent_location])

		if (self.heap_array[parent_location].value< element.value):
		#	print ("need to replace")
			tmp=self.heap_array[parent_location]
			self.heap_array[parent_location]=element
			self.heap_array[current_location]=tmp

		#	print ("after replace",self.heap_array)
			current_location=parent_location
			self.percolate_up(element,current_location+1)
		#	print ("returning")
		else:
		#	print ("no more percolating")
			return 
		#print ("Finished--->")
		#for item in self.heap_array:
		#	print item.key, item.value


	def percolate_down(self,element,current_location): #current location in current_index+1
		left_child_location=(2*current_location)-1
		right_child_location=(2*current_location+1)-1
		
		current_location=current_location-1


		if left_child_location > self.heapsize-1 or right_child_location  >= self.heapsize-1:
			return



		if self.heap_array[right_child_location].value > self.heap_array[left_child_location].value :
			child_location=right_child_location
		else:
			child_location=left_child_location

		#print ("child_location:",child_location, "; current_location:",current_location)



		if self.heap_array[current_location].value < self.heap_array[child_location].value:
			tmp=self.heap_array[child_location]
			self.heap_array[child_location]=element
			self.heap_array[current_location]=tmp
		#	print ("after replace",self.heap_array)
			current_location=child_location
			self.percolate_down(element,current_location+1)


	def get_heap(self):
		print (self.heap_array)
"""

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
	
"""
#######################
import random


random_list = [random.randint(0,100) for i in range(10000)]

#print l

dict_count={}


for i in range(0, len(random_list)):
	element=random_list[i]
	try:
		x=dict_count[element]
		dict_count[element]+=1
	except:
		dict_count[element]=1



#for item in dict_count:
#	print item, dict_count[item]
	#pp	


i=0

#heap=BinaryMaxHeap()
"""
node1=Node('a',1)
node2=Node('b',3)
node3=Node('c',2)
node4=Node('d',5)
node5=Node('e',8)
node6=Node('f',6)
node7=Node('g',1)
node8=Node('i',9)
heap=BinaryMaxHeap()

heap.insert_element(node1)
heap.insert_element(node2)
heap.insert_element(node3)
heap.insert_element(node4)
heap.insert_element(node5)
heap.insert_element(node6)
heap.insert_element(node7)
heap.insert_element(node8)

"""
#pp


heap=BinaryMaxHeap()

i=0
for item in dict_count:
	node=Node(item, dict_count[item])
	if i < 10:
		heap.insert_element(node)
	i=i+1
	#print item, dict_count[item]
	#print "heap size", heap.heapsize
	if i >=10: #stop growing the heap. instead start deleting and replacing
		#current_minimum_heapindex=heap.heap_array[-1]
		min_index=heap.find_minimum_element_loc()


		current_minimum_heapelement=heap.heap_array[min_index]

		if node.value > current_minimum_heapelement.value:
			
			heap.heap_array[min_index]=node
			heap.percolate_up(node, min_index+1)
			
		#print minimum_element.key, minimum_element.value


for item in heap.heap_array:
	print item.key, item.value



import operator

#d = {"a":1, "b":2, "c":3}
cd = sorted(dict_count.items(),key=operator.itemgetter(1),reverse=True)
print cd [0:10]


		
