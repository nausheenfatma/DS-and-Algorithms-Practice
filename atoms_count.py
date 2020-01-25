class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None


class Stack:
	def __init__(self):
		self.top=None


	def push(self,data):
		node=Node(data)
	
		if self.top==None: #first element
			self.top=node
		else:
			node.prev=self.top
			self.top=node


	def peek(self):
		if self.top!=None:
			return self.top.data
		else:
			print "stack is empty"
			return None

	def pop(self):
		if self.top!=None:
			popped=self.top
			self.top=self.top.prev
			return popped.data
		else:
			print "stack is empty"
			return None





import operator

if __name__=="__main__":

	"""
	s=Stack()
	s.push(1)
	s.push(2)
	s.push(3)

	print s.pop()
	print s.pop()	
	print s.pop()
	print s.pop()
	"""


	expression="K4(ON(SO3)20)2"

	#expression="Mg(OH)21"

	#expression="Be32"

	exp_len=len(expression)

	s=Stack()


	index=0

	while index < len(expression):
		symbol=expression[index]

		#print "symbol",symbol

		if symbol.islower():
			popped=s.pop()
			(x,y)=popped	
			x+=symbol
			s.push((x,y))

		if symbol=="(":
			#s.push({"symbol":"(","count":0})
			s.push(("(",0))

		if symbol.isalpha() and not symbol.islower() :
			#itemcount={"symbol":symbol,"count":1}
			itemcount=(symbol,1)
			s.push(itemcount)

		if symbol.isdigit():
			dig=symbol
			while True:
				if index+1 < len(expression) and  expression[index+1].isdigit():
					index=index+1
					dig+=expression[index]
				else:
					break
				
			

			number=int(dig)
			popped=s.pop()
			(x,y)=popped	
			y*=number
			s.push((x,y))

		if symbol==")":
			hold_elements=[]
			while True:
				(x,y)=s.pop()
				#if x["symbol"]=="(":
				if x=="(":
					break
				else:
					hold_elements.append((x,y))

			#print "hold_elements",hold_elements
			#dig=""
			flag=False
			dig=""
			while True:
				

				if index+1 < len(expression) and  expression[index+1].isdigit():
					flag=True
					index=index+1
					#print "expression[index]",expression[index]
					dig+=expression[index]
				else:
					break

			if flag==True:
				number=int(dig) #multiplier
			else:
				number=1
				


			for item in hold_elements:
					(x,y)=item
					
					y*=number
					s.push((x,y))

		index+=1
	atom_count={}
	while True:
		if s.peek()==None:
			break
		(x,y)=s.pop()
		try:	
			atom_count[x]=atom_count[x]+y
		except:
			atom_count[x]=y

	
	sorted_x = sorted(atom_count.items(), key=operator.itemgetter(0))
	countformula=""
	for item in sorted_x:
		(x,y)=item
		if y!=1:
			countformula=countformula+x+str(y)
		else:
			countformula=countformula+x

	return countformula

	

