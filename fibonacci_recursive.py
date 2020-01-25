
#recursive

def fibonacci(n):
	if n==1 or n==2: #base case
		return 1

	fib_n=fibonacci(n-1)+fibonacci(n-2) #recursive step
	return fib_n


#x= fibonacci(6)
#print x


#iterative--use for loops


def  fibonacci(n):
	if n==1 or n==2: #base case
		return 1
	else:
		n1=1
		n2=1
		for i in range(2,n):
			n3=n1+n2
			n1=n2
			n2=n3

		return n3


x= fibonacci(4)
print x


	






