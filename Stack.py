"""
Implement Stack using LinkedList
"""

class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None


class Stack:
	def __init__(self):
		self.top=None
	
	def push(self,data):
		node=Node(data)
		if self.top==None: #stack is empty
			print "first element"
			self.top=node
		else :
			print "new elements"
			node.prev=self.top  #save address of previous node
			self.top=node

	def pop(self):
		popped=None
		if self.top!=None:
			popped= self.top.data
			self.top=self.top.prev
			
		else:
			print "Stack is empty"
		return popped
		

def main():
	s=Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	print s.pop()
	print s.pop()
	print s.pop()	
	print s.pop()	
	print s.pop()	


if __name__=="__main__":
	main()
		
