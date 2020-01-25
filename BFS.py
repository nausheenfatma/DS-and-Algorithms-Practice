#####################################################################################
class ListNode:
	def __init__(self,data):
		self.data=data
		self.next=None
			
class GraphNode:
	def __init__(self,vertex):
		self.vertex=ListNode(vertex)
		self.list=None
		#self.next=None

	def addlist(self,listitems):
		if len(listitems)>0: #first item of the list (excluding vertex)
			head=ListNode(listitems[0])
			prev_node=head
			self.list=head
			if len(listitems)>1:

				for item in listitems[1:]:
					listnode=ListNode(item)
					prev_node.next=listnode
					prev_node=listnode

class Graph:
	def __init__(self):
		self.V=[1,2,3,4,5,6,7,8,9] #vertices list
		self.graph=[]	#graph= array of GraphNodes instances

		self.dataToGraphNode={} #stores address of adjacenecy list items

		#initalize and build graph
		vertextlistitems={1:[2], 2:[1,3,4], 3:[2,4,6], 4:[2,3,5], 5:[4,6,7], 6:[5,8], 7:[], 8:[9], 9:[]}


		for vertex in vertextlistitems:
			graph_node=GraphNode(vertex)
			vertexlist=vertextlistitems[vertex]
			graph_node.addlist(vertexlist)
			self.dataToGraphNode[vertex]=graph_node
			self.graph.append(graph_node)
		print len(self.graph)

		for item in self.graph:
			print "-----------------------------"
			print "main head--",item.vertex.data
			
			adj_list= item.list

			headpointer=adj_list
			while headpointer!=None:
				#print headpointer.data
				headpointer=headpointer.next

#####################################################################################
class QueueNode:
	def __init__(self,queueitem):
		self.queueitem=queueitem
		self.prev=None


class Queue:
	def __init__(self):
		self.first=None
		self.last=None
	
	def Enqueue(self,queueitem):
		node=QueueNode(queueitem)
		if self.last==None or self.first==None: #stack is empty
			#print "first element"
			self.first=node
			self.last=node
		else :
			#print "new elements"
			self.last.prev=node #save address of previous node
			self.last=node

	def Dequeue(self):
		popped=None
		if self.first!=None:
			popped= self.first.queueitem
			self.first=self.first.prev
			
		else:
			print "Queue is empty"
		return popped
#####################################################################################

def BFS(visited, mygraph, myqueue):

	while myqueue.first!=None:
		print "--------------------------------------------------------------------"
		q_item=myqueue.Dequeue() #queue node
		print "visiting---", q_item.vertex.data
		#put all items in adjacency list in the queue

                visited[q_item.vertex.data]=1
		#print visited
		adj_list= q_item.list
			

		headpointer=adj_list
		#headpointer.data
		"""

		while headpointer!=None:
				#print "adding elements in queue"
				current_node=mygraph.dataToGraphNode[headpointer.data]
				#print current_node.vertex.data, headpointer.data

			
				if visited[current_node.vertex.data]==0:
					print "adding in queue",current_node.vertex.data
					myqueue.Enqueue(current_node)
				else:
					print "already visited",current_node.vertex.data
				
				headpointer=headpointer.next

		"""
#main code starts below#########################################################

mygraph=Graph()
visited={ i:0 for i in  mygraph.V}
myqueue=Queue()

if mygraph!=None and  len(mygraph.graph) >0:
	current_graph_node=mygraph.graph[0]
	print "DFS below"
	myqueue.Enqueue(current_graph_node)
	BFS(visited,mygraph, myqueue)


