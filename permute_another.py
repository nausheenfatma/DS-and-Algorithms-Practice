
ways=[]
def permute(stringtext, permutedstring=""):
	if len(stringtext)==0:
		ways.append(permutedstring)
		return

	for i in range (0,len(stringtext)):
		candidate=stringtext[i]
		remaining= stringtext[0:i]+stringtext[i+1:]
		permute(remaining, permutedstring+candidate)


permute("1234","")
print ways


