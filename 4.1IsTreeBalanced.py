"""
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one

answer: difference of min depth and max depth should not be greater than 1
order:o(n)

"""

class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None



class Tree:
	def __init__(self,root):
		self.root=root
	


	def insert_left_node(self,parent_node,child_node):
		parent_node.left=child_node


	def insert_right_node(self,parent_node,child_node):
		parent_node.right=child_node


	def inorder_traversal(self,root):
		if root==None:
			return

		self.inorder_traversal(root.left)
		print root.data
		self.inorder_traversal(root.right)



	def max_height(self,root):

		if root==None:
			return 0
		left_height=self.max_height(root.left)
		right_height=self.max_height(root.right)
		print "root",root.data, 1+max(left_height,right_height)
		return 1+max(left_height,right_height)

	def min_height(self,root):

		if root==None:
			return 0
		left_height=self.min_height(root.left)
		right_height=self.min_height(root.right)
		print "root",root.data, 1+min(left_height,right_height)
		return 1+min(left_height,right_height)


def main():
	rootnode=Node(1)			#1
	tree=Tree(rootnode)

	node2=Node(2)	
	tree.insert_left_node(rootnode,node2)	

	node3=Node(3)			#2		3
	tree.insert_right_node(rootnode,node3)		

	node4=Node(4)	
	tree.insert_left_node(node2,node4)									
	node5=Node(5)		#4	    5	     6		7
	tree.insert_right_node(node2,node5)   #   10      		                8     											11		9
	node6=Node(6)	
	tree.insert_left_node(node3,node6)									
	node7=Node(7)	
	tree.insert_right_node(node3,node7)	
	node8=Node(8)	
	tree.insert_right_node(node7,node8)	
	node9=Node(9)	
	tree.insert_right_node(node8,node9)	

	node10=Node(10)	
	tree.insert_left_node(node6,node10)


	node11=Node(11)	
	tree.insert_left_node(node8,node11)
	#tree.inorder_traversal(rootnode)

	max_height=tree.max_height(rootnode)
	min_height=tree.min_height(rootnode)
	print max_height,min_height

if __name__=="__main__":
	main()


								



		
			
