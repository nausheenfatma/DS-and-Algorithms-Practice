"""
Input = 1,3,6,7,10,20,21
"""



class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


class BinarySearchTree:

	def __init__(self,root):
		self.root=root


	def insert_bst(self,root,node):

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




def main():
	rootnode=Node(1)			#1
	tree=BinarySearchTree(rootnode)
	node2=Node(2)	
	tree.insert_bst(rootnode,node2)	
	print "---------------------------------------"
	node3=Node(3)			#2		3
	tree.insert_bst(rootnode,node3)		
	print "---------------------------------------"
	node4=Node(4)	
	tree.insert_bst(rootnode,node4)		
	print "---------------------------------------"							
	node5=Node(5)		#4	    5	     6		7
	tree.insert_bst(rootnode,node5)   #   10      		                8    
	print "---------------------------------------"							 #											11		9	
	tree.inorder_traversal(rootnode) 


if __name__=="__main__":
	main()
