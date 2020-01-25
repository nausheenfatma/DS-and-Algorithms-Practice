sum_array=[]

max_seen_so_far=float('-inf')


class Solutiom

def LCS(arr, prev_sum=-100):
	if len(arr)==0:
		return max_seen_so_far
	else:

		current_sum =max(prev_sum+arr[0], arr[0])

		max_seen_so_far=max(max_seen_so_far,cuurent_sum)

		#sum_array.append(current_sum)
		
		LCS(arr[1:],current_sum)

	return max_seen_so_far


arr=[-2,1,-3,4,-1,2,1,-5,4]


print sum_array
print LCS(arr)

