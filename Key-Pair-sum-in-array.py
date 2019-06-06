## Key PAir
## Given an array A of N positive integers and another number X. 
## Determine whether or not there exist two elements in A whose sum is exactly X.
#6 16
#1 4 45 6 10 8
#5 10
#1 2 4 3 6
## O/p : Yes, Yes

## Method: Hashing
## Time complexity : O9n{, space: O(n)

def key_pair(arr,n,sum):
    
    s=set()
    
    for i in range(0,n):
        temp=sum-arr[i]
        
        if temp >=0 and temp in s:
            print("Pair is",arr[i],",",temp)
            
        s.add(arr[i])
        
A = [1,4,45,6,10,8] 
n = 16
key_pair(A,len(A),n)
        
