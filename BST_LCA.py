"""
Input = 1,3,6,7,10,20,21
"""



class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


class BinarySearchTree:

	def __init__(self):
		self.root=None


	def insert_bst(self,root,node):
		if root==None:
			self.root=node
			return

		if node.data <= root.data:
			if root.left==None:
				root.left=node
			else:
				self.insert_bst(root.left,node)
			

		if node.data > root.data:
			if root.right==None:
				root.right=node
			else:
				self.insert_bst(root.right,node)



	def inorder_traversal(self,root):
		if root==None:
			return

		self.inorder_traversal(root.left)
		print root.data
		self.inorder_traversal(root.right)

	def find_LCA(self,root,a,b):
		if root==None:
			return
		#print root.data
		if a<root.data and root.data < b:
			print "this",root.data
			return 
		self.find_LCA(root.left,a,b)

		self.find_LCA(root.right,a,b)


	def find_inrange_data(self,root,a,b):
		if root==None:
			return

		self.find_inrange_data(root.left,a,b)
		#print root.data
		if a<=root.data and root.data <= b:
			print "this",root.data
			#return 
		self.find_inrange_data(root.right,a,b)

   
#fails for 1 edge case when 11,18 when 11 is an ancestor of 18



def main():

	tree=BinarySearchTree()
	rootnode=Node(10)			#			10
	tree.insert_bst(None,rootnode)		#
	node2=Node(5)				#		5		21
	tree.insert_bst(rootnode,node2)	
	node2=Node(21)	
	tree.insert_bst(rootnode,node2)	
	node2=Node(11)				#		   6	    11		27
	tree.insert_bst(rootnode,node2)	
	node2=Node(6)	
	tree.insert_bst(rootnode,node2)	
	node2=Node(15)				#				 15	
	tree.insert_bst(rootnode,node2)		#					18
	node2=Node(18)	
	tree.insert_bst(rootnode,node2)	
	node2=Node(27)	
	tree.insert_bst(rootnode,node2)	

	tree.inorder_traversal(rootnode)
	tree.find_LCA(rootnode,15,27)
	#tree.find_inrange_data(rootnode,6,15)
if __name__=="__main__":
	main()
