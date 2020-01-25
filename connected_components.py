arr=[[1,0,1,1,1],
     [1,0,1,0,0],
     [1,0,1,0,0],
     [1,0,1,0,0],
     [1,1,1,0,0],
    ]


arr=[[1,0,1,1,1],
     [1,0,1,0,1],
     [1,1,1,0,1]]

def DFS(arr,current_i,current_j):
	if current_i <0 or current_i >=len(arr):
		return 0

	if current_j <0 or current_j >=len(arr[0]):
		return 	0

	if arr[current_i][current_j]==1:


		print "visiting",current_i,current_j
		
		arr[current_i][current_j]=-1 # to mark visited, overwrite with -1

		if current_j-1>=0:
			left=arr[current_i][current_j-1]
			if left ==1 :
				val=DFS(arr,current_i,current_j-1)

		if current_j+1 < len(arr[0]):
			right=arr[current_i][current_j+1]
			if right==1:
				val=DFS(arr,current_i,current_j+1)

		if current_i-1 >=0: 
			top=arr[current_i-1][current_j]
			if top ==1:
				val=DFS(arr,current_i-1,current_j)

		if current_i+1 < len(arr):
			bottom=arr[current_i+1][current_j]
			if bottom==1:
				val=DFS(arr,current_i+1,current_j)
	else:	#current node is not 1
		print "no path, returning from", current_i,current_j
		return 0
	return 1 #when all the paths from the node has been explored


def run():

	components=0
	for row in range(len(arr)):
		for column in range(len(arr[row])):
			components+=DFS(arr,row,column)
			print "components--",components


	return val


print "starting----------"
components=run()
print components
