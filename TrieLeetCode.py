class Trie(object):

    def __init__(self):
		self.children=[None]*26 #array of addresses 
		self.isEndOfWord=False
        	self.root=self
        	self.prefixWordList=None
        
        

    def insert(self, word):
		wordLength=len(word)
		current_node=self.root

		for alphabet in word:
			#check if node is present
			index=self.charToIndex(alphabet)
			if current_node.children[index]==None:#if not present add node
				node=Trie()
				current_node.children[index]=node
				#print "not present",alphabet
			else:
				node=current_node.children[index] #if present
				#print "was present",alphabet
			
			current_node=node

		current_node.isEndOfWord=True
		#current_node.value=meaning
		#print "inserted",word
            	return None
        

    def search(self, word):
		current_node=self.root
		word_length=len(word)
		isPresent=True
		for alphabet in word:
			print alphabet
			index= self.charToIndex(alphabet)
			if current_node.children[index]!=None:
				current_node=current_node.children[index]
			else :
				isPresent=False
				break
		if current_node.isEndOfWord==True and isPresent=True:
			pass
		else:
			isPresent=False
        	return isPresent
    

    def startsWith(self, prefix):
		current_node=self.root
        	found=True
		for alphabet in prefix:
			index= self.charToIndex(alphabet)
			print alphabet
			if current_node.children[index]!=None:
				current_node=current_node.children[index]
			else :
                		found=False
				break	
	
		#self.prefixWordList=[]
		#seensofar=prefix
		#print "seensofar",seensofar
		#nodeAddress=current_node        
       		return found

    def charToIndex(self,ch): 
        	return ord(ch)-ord('a') 

    def indexToChar(self,index): 
		#print chr(index)
        	return chr(index)
        

        
if __name__=="__main__":

	trie=Trie()
	trie.insert("hello")
	print trie.search("hell")
	print trie.search("helloa")


	pp
	trie.insert("app")
	trie.insert("apple")
	trie.insert("apples")
	trie.insert("applesinthekitchen")
	trie.insert("but")
	trie.insert("butt")
	trie.insert("butter")



	#print "retrieval-------"
	print trie.search("a")
	print trie.search("app")
	print trie.search("apple")
	print trie.search("appl")
	print trie.search("applesi")
	#trie.search("")
	print trie.startsWith("apy")





