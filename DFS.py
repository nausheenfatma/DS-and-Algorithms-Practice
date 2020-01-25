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
		self.V=[0,1,2,3,4] #vertices list
		self.graph=[]	#graph

		self.dataToGraphNode={}

		#initalize graph
		vertextlistitems={0:[0,1,2], 1:[0], 2:[4], 3:[3,4], 4:[0]}

		for vertex in vertextlistitems:
			graph_node=GraphNode(vertex)

			vertexlist=vertextlistitems[vertex]

			graph_node.addlist(vertexlist)
			self.dataToGraphNode[vertex]=graph_node
			
			self.graph.append(graph_node)

		"""
		print len(self.graph)

		for item in self.graph:
			print "-----------------------------"
			print "main head--",item.vertex.data
			
			adj_list= item.list

			headpointer=adj_list
			while headpointer!=None:
				#print headpointer.data
				headpointer=headpointer.next
		"""

########################################################################
def DFS(current_node, visited,mygraph):
	############################################################	
	if current_node==None :
		print "none found,returning"

	if visited[current_node.vertex.data]==1:
		print "already visited--",current_node.vertex.data
	############################################################	
	if current_node==None or visited[current_node.vertex.data]==1:
		return
	else:
		print "visiting", current_node.vertex.data
		visited[current_node.vertex.data]=1

		adj_list= current_node.list

		headpointer=adj_list


		while headpointer!=None:
				current_node=mygraph.dataToGraphNode[headpointer.data]
				DFS(current_node, visited, mygraph)
				headpointer=headpointer.next





#main code starts below#########################################################


mygraph=Graph()
visited={ i:0 for i in  mygraph.V}


if mygraph!=None and  len(mygraph.graph) >0:
	current_graph_node=mygraph.graph[0]
	print "DFS below"
	DFS(current_graph_node, visited,mygraph)





		


