arr=[[1,0,0,0,0],
     [1,0,1,1,0],
     [0,1,0,1,0],
     [0,1,1,1,1],
     [1,0,0,0,0],
    ]


rows,columns=len(arr),len(arr[0])
nodes=max(rows,columns)

visited=[[0]*len(arr[0])]*len(arr)
 

def DFS(arr,current_i,current_j,target_i,target_j):
	if current_i <0 or current_i >=len(arr):
		return 0

	if current_j <0 or current_j >=len(arr[0]):
		return 	0

	print "visiting",current_i,current_j
	
		
	if current_i == target_i and current_j ==target_j:
		return 1



	val=0
	arr[current_i][current_j]=-1


	#going left

	if current_j-1>=0:
		left=arr[current_i][current_j-1]
		if left ==1 :
			val=DFS(arr,current_i,current_j-1,target_i,target_j)
			if val==1:
				return 1

	#going right
	if current_j+1 < len(arr[0]):
		right=arr[current_i][current_j+1]
		if right==1:
			val=DFS(arr,current_i,current_j+1,target_i,target_j)
			if val==1:
				return 1

	#going top
	if current_i-1 >0: 
		top=arr[current_i-1][current_j]
		if top ==1:
			val=DFS(arr,current_i-1,current_j,target_i,target_j)
			if val==1:
				return 1


	#going below
	if current_i+1 < len(arr):
		bottom=arr[current_i+1][current_j]
		if bottom==1:
			val=DFS(arr,current_i+1,current_j,target_i,target_j)
			if val==1:
				return 1
	print "returning",val
	return val


def run():
	source_i,source_j=1,2
	target_i,target_j=3,1
	val=DFS(arr,source_i,source_j,target_i,target_j)
	print val


print "starting----------"
run()

