#Count distinct elements in every window of size k.

from collections import defaultdict
def distinct_window(arr,k,n):
    my_dict=defaultdict(lambda:0)
    dist_count=0
    
    for i in range(k):
        #print(my_dict[arr[i]])
        if my_dict[arr[i]] == 0:
            dist_count+=1
        my_dict[arr[i]]+=1
        
    print(str(dist_count))
    
    for i in range(k,n):
        if my_dict[arr[i-k]] ==1:
            dist_count-=1
        my_dict[arr[i-k]]-=1
        
        if my_dict[arr[i]] == 0:
            dist_count+=1
        my_dict[arr[i]]+=1
        
        print(dist_count)
            
    
    
arr = [1, 2, 1, 3, 4, 2, 3] 
n = len(arr) 
k = 4
distinct_window(arr,k,n)