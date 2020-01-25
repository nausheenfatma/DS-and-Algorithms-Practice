def LCS (str1, str2, match_str= ""):

	 
	if len(str1)==0 or len(str2)==0:
		return 0, match_str


	if str1[-1]==str2[-1]: 
		max_val, match_str=LCS(str1[:-1], str2[:-1], match_str)
		match_str+=str1[-1]
		return 1+ max_val, match_str


	else :
		max_val, match_str=max(LCS(str1[:-1], str2, match_str ),LCS(str1, str2[:-1]), match_str)
		return max_val, match_str


print LCS ("helloworld","hell0 world!", "")

	

