"""

How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.

"""

class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
	


class Stack:
	def __init__(self):
		self.top=None
		
	
	def push_min(self,data):
		node=Node(data)
		print "pushing",data
		if self.top==None: #stack is empty
			print "first element"
			self.top=node
		else :
			print "new elements"
			popped=self.pop()
			popped=Node(popped)
			print popped.data, node.data
			if popped.data < node.data:	
				print "popped.data < node.data True"
				node.prev=self.top  #save address of previous node
				self.top=node

				popped.prev=self.top  #save address of previous node
				self.top=popped
			else:
				print "popped.data < node.data False"
				popped.prev=self.top  #save address of previous node
				self.top=popped

				node.prev=self.top  #save address of previous node
				self.top=node

		print "----------------------------------"

	def peek(self):
		return self.top.data


	def push(self,data, min_stack ):
		node=Node(data)

		if self.top==None: #first element

			self.top=node  #both nodes are top
			min_stack.top=node
			#self.current_min=data

		else :
			node.prev=self.top
			self.top=node
			
			if data <  min_stack.peek(): 
				min_node=Node(data)
				min_node.prev=min_stack.top
				min_stack.top=min_node


		print "min is ", min_stack.peek()
				#self.current_min=data


	def min_value(self,min_stack):
		if min_stack.peek()!=None:
			print "min",min_stack.peek()
		else :
			print "min is empty"
		


	def pop(self,min_stack):
		popped=None
		if self.top!=None:
			popped= self.top.data
			print "popping", popped
			self.top=self.top.prev

			if popped==min_stack.peek():
				print "popping min", min_stack.peek()
				min_stack.top=min_stack.top.prev
			
		else:
			print "Stack is empty"
		return popped
		

def main():
	stack=Stack()
	min_stack=Stack()
	stack.push(3,min_stack)
	stack.push(4,min_stack)
	stack.push(2,min_stack)
	stack.push(6,min_stack)
	stack.push(1,min_stack)


	stack.pop(min_stack)
	print min_stack.peek()


	stack.pop(min_stack)
	print min_stack.peek()


	stack.pop(min_stack)
	print min_stack.peek()


	stack.pop(min_stack)
	print min_stack.peek()


	stack.pop(min_stack)
	#print min_stack.peek()	

if __name__=="__main__":
	main()
		
