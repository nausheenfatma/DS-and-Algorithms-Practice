class Solution(object):

   def merge(self,arr1, arr2):
	index_1=0
	index_2=0
	merged_list=[]

	while index_1< len(arr1) and index_2 <len(arr2):
		if arr1[index_1] < arr2[index_2]:
			merged_list.append(arr1[index_1])
			index_1+=1
		else:
			merged_list.append(arr2[index_2])
			index_2+=1

	if index_1==len(arr1):
		merged_list=merged_list+arr2[index_2:]
	else:
		merged_list=merged_list+arr1[index_1:]
	print "arr1",arr1
	print "arr2",arr2
	print "merged_list",merged_list
	print "----------------------------"
	return merged_list

   def divide(self,arr):

	if len(arr)==1:
		print "cant divide return", arr
		return arr

	print "Divide", arr
	if len(arr) >1:
		mid=int(len(arr)/2)
		first_half=arr[0:mid]
		second_half=arr[mid:]
		merged=self.merge(self.divide(first_half),self.divide(second_half))

		print "returning merged",merged
		return merged







s=Solution()
print s.divide([5,2,6,1,0,9,3,4,3])

