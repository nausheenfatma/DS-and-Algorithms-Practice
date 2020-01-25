"""
Input = 1,3,6,7,10,20,21


Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
"""

#1 2 3 4


class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


class BinarySearchTree:

	def __init__(self,root):
		self.root=root


	def insert_bst(self,root,node):
		if root==None:
			self.root=node
			print "no root",node
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


	def build(self,beg,end,array_list):

		mid=int((beg+end)/float(2))
		nodeatmid=Node(array_list[mid])
		print "nodeatmid",nodeatmid.data
		#print "self.root",self.root.data
		self.insert_bst(self.root,nodeatmid)
		if beg==mid :
			return
		        

		self.build(beg,mid,array_list)
		self.build(mid+1,end,array_list)


	def max_height(self,root):

		if root==None:
			return 0
		left_height=self.max_height(root.left)
		right_height=self.max_height(root.right)
		print "root",root.data, 1+max(left_height,right_height)
		
		return 1+max(left_height,right_height)




def main():

	array_list=[1,3,6,7,10,20,21]
	tree=BinarySearchTree(None)
	array_len=len(array_list)
	tree.build(0,array_len-1,array_list)

	##################################################################################
	"""

	rootnode=Node(4)			#1
	tree=BinarySearchTree(None)
	
	tree.insert_bst(None,rootnode)	
	node2=Node(2)	
	tree.insert_bst(rootnode,node2)	
	print "---------------------------------------"
	node3=Node(3)			#2		3
	tree.insert_bst(rootnode,node3)		
	print "---------------------------------------"
	node4=Node(1)	
	tree.insert_bst(rootnode,node4)		
	print "---------------------------------------"							
	node5=Node(5)		#4	    5	     6		7
	tree.insert_bst(rootnode,node5)   #   10      		                8    
	print "---------------------------------------"							 #

	node6=Node(6)		#4	    5	     6		7
	tree.insert_bst(rootnode,node6)   #   10      		                8    
	print "---------------------------------------"							 #								
	"""



	tree.inorder_traversal(tree.root) 
	height=tree.max_height(tree.root)
	print "height",height
	##################################################################################
if __name__=="__main__":
	main()
