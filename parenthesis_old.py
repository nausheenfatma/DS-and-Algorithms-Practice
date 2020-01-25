expression_list=[]


def generateParenthesis(expr, leftbracketcount, rightbracketcount):
	if leftbracketcount==0 and rightbracketcount==0 :
		print "adding", expr
		expression_list.append(expr)
		return


	if leftbracketcount==rightbracketcount:
		generateParenthesis(expr+"(", leftbracketcount-1, rightbracketcount)
	else:

		if leftbracketcount!=0:
			generateParenthesis(expr+"(", leftbracketcount-1, rightbracketcount)	

		if rightbracketcount!=0:
			generateParenthesis(expr+")", leftbracketcount, rightbracketcount-1)


generateParenthesis('',4,4)
print expression_list
