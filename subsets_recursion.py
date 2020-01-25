#subsets_list=[]

#all_subsets=set()
all_subsets=[]

def find_subsets(arr, subset):
	all_subsets.append(subset)



	for i in range(0, len(arr)):
		print "------------------",i
		print "here",i,arr, arr[i+1:], subset+[arr[i]]
		find_subsets(arr[i+1:], subset+[arr[i]])
		print "back",arr,subset,i,len(arr)-1


find_subsets([1,2,3,4],[])
print "all", all_subsets


