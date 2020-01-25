"""
Implement Queue using LinkedList
"""

class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None


class Queue:
	def __init__(self):
		self.first=None
		self.last=None
	
	def enqueue(self,data):
		node=Node(data)
		if self.last==None: #stack is empty
			#print "first element"
			self.first=node
			self.last=node
		else :
			#print "new elements"
			self.last.prev=node #save address of previous node
			self.last=node




	def dequeue(self):
		popped=None
		if self.first!=None:
			popped= self.first.data
			self.first=self.first.prev
			
		else:
			print "Queue is empty"
		return popped
		

def main():
	s=Queue()
	s.enqueue(1)
	s.enqueue(2)
	s.enqueue(3)
	s.enqueue(4)
	s.enqueue(5)
	print s.dequeue()
	print s.dequeue()
	print s.dequeue()	
	print s.dequeue()	
	print s.dequeue()	


if __name__=="__main__":
	main()
		
