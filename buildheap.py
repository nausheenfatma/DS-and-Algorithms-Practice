# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 08:54:43 2017

@author: nausheenfatma
"""


#In-place heapify algorithm

def heapify(data,node_index,n):

        i=node_index
        left_child_index=2*i+1
        right_child_index=2*i+2
        #print left_child_index,right_child_index
        
        
        print "i",i
        print "data", data[i]
        
        if i > n/2-1:
            print "leaf return"
            return        
        
        
        bigger_child_index=left_child_index
        
            
        if left_child_index<n & right_child_index<n:
                if data[left_child_index] < data[right_child_index]:
                    bigger_child_index=right_child_index
                
        if data[bigger_child_index]>data[i]:
                print "percolateing down at index",bigger_child_index
                print "swapping with",data[bigger_child_index]
                temp=data[i]
                data[i]=data[bigger_child_index]
                data[bigger_child_index]=temp
                print "data",data
                
                
        heapify(data,bigger_child_index,n)     

        
#Array data as complete binary tree
#parent index=|_ (i-1)/2 _|
#left_child= 2*i+1
#right_child=2*i+2
#first_non_leaf_node= |_ n/2 _| -1 where n=number of objects
def main():       
    data=[1,3,2,9,6,16,4]
    
    n=len(data)
    
    first_non_leaf_node_index= n/2 -1
    non_leaf_node_index=first_non_leaf_node_index
    
    
    
    print data
                
    for k in range(non_leaf_node_index,-1,-1):
            #print "i", k
            heapify(data,k,n)
            
    
    
    print "---------------------------"          
    print "Output Heap :"   
         
    print data
    print "---------------------------"          
    print "Complexity=nlogn"   
    print "---------------------------"         


if __name__=="__main__": 
    main()
    