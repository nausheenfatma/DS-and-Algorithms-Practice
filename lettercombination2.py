mapping= { 2:["a", "b", "c" ], 3: ["d", "e", "f"], 4:["g", "h", "i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p", "q", "r","s"], 8:["t","u","v"],9:["w","x", "y", "z"]}

def letterCombinations(digits):
	if len(digits) ==1:
			arr=mapping[int(digits)]
			return arr

        if len(digits) ==0:
                return []

	words=[]
	left=digits[0] #one character wise
	right=digits[1:]

	left_arr=mapping[int(left)]
	right_arr=letterCombinations(right)

	for i in left_arr:
		for k in right_arr:
			words.append(i+k)
	#print "left_arr",left_arr
	#print "right_arr",right_arr 
	#print "words", words
	print "-----------------------"
	return words


words=letterCombinations("234") #len digits- M , number of characters per digit=N

#O(M,N)

print words, len(words)

