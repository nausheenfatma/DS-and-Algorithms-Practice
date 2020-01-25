#using queues

#prerequisites=[ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],[3,8], [4,5], [4,9], [7,8], [7,9] ]
#numCourses=10

prerequisites=[ [0,1], [1,0]]
numCourses=3
print "prerequisites",prerequisites
print "--------------------------------------------------------------------------"

class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None

class Queue:
	def __init__(self):
		self.head=None
		self.tail=None


	def Enqueue(self,data):
		node=Node(data)
		if self.head ==None:
			#print "first"
			self.head=node
			self.tail=node
			#print self.head
		else:
			self.tail.prev=node
			self.tail=node


	def Dequeue(self):
		#print self.head
		if self.head==None:
			print "Empty"
			return None
		node=self.head
		#print node.data
		self.head=self.head.prev

		return node.data

	def IsQueueEmpty(self):
		if self.head==None:
			return True
		else:
			return False



###
"""
q=Queue()


q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)

print q.Dequeue()
print q.Dequeue()
print q.Dequeue()
print q.Dequeue()
print q.Dequeue()
pp
"""

def canFinish( numCourses, prerequisites):
	indegrees={}

	out_neighbours={}

	for i in range(0,numCourses):
		indegrees[i]=0
		out_neighbours[i]=[]

	for preq in prerequisites:
		source,target=preq[0],preq[1]
		indegrees[target]+=1
		out_neighbours[source].append(target)


	q=Queue()
	
	for item in indegrees:
		if indegrees[item]==0:
		
			q.Enqueue(item)

	counter=0
	
	#print "indegrees",indegrees
	while q.IsQueueEmpty() ==False:

		counter+=1

		node_item=q.Dequeue()
		print "node_item",node_item


		for out_neighbour in out_neighbours[node_item]:
			#print "out_neighbour",out_neighbour, indegrees[out_neighbour]
			indegrees[out_neighbour]-=1
			#print "out_neighbour",out_neighbour, indegrees[out_neighbour]
			#print "indegrees",indegrees
			if indegrees[out_neighbour]==0:
				q.Enqueue(out_neighbour)

		#print "updated all after removing ========================",node_item
	print "Counter",counter

	if counter!=numCourses:
		return False
	else :
		return True
	


	

canFinish(numCourses,prerequisites)
	
		
		

	
	
