"""
Reverse stack without buffer
"""


class Node:
	def __init__(self,data):
		self.data=data
		self.below=None


class Stack:
	def __init__(self):
		self.top=None

	def push(self,data):
		node=Node(data)
			
		if self.top==None: #stack is empty
			self.top=node
		else:
			node.below=self.top
			self.top=node


	def peek(self):
		if self.top==None:
			print "stack is empty"
		else :
			return self.top.data


	def pop(self):
		popped=None
		if self.top==None:
			print "stack is empty"
		else:
			popped=self.top.data
			self.top=self.top.below

		return popped

	def reverse(self):
		

		if self.top==None: #base case is satisfied just once
			print "self.top==None in reverse method"
			return
		data=self.pop()
		print data
		self.reverse()
		#self.push(data)
		#print "insert at bottom---",data
		print "insertatbottom(",data,")-----------------------------------------------------------------"
		self.insertatbottom(data)

	def insertatbottom(self,data):
		print "inside insertatbottom(",data,")"		
		if self.top==None:
			print "self.top==None in insertatbottom"
			print "pushing after none found--",data
			self.push(data)
			return
		temp=self.pop()
		print "temp---",temp
		print "data---",data
		print "peek(self)",self.peek()
		self.insertatbottom(data)
		print "pushing--",temp
		self.push(temp)

		





def main():
	s=Stack()
	s.push(6)
	s.push(5)
	s.push(4)
	s.push(3)
	s.push(2)
	s.push(1)
	print "pushed all data"
	s.reverse()

	print s.pop()
	print s.pop()	
	print s.pop()
	print s.pop()
	print s.pop()
	print s.pop()

if __name__=="__main__":
	main()


	
	
