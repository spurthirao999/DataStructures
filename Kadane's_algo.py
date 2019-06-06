## Kadane's algorithm
## Largest Sum contigious array
## DP: Maximum Sum subsequence
## [-2 -3 4 -1 -2 1 5 -3] SUm=4-1-2+1+5=7


def kadanes_algorithm(arr,n):
    
    max_ending_here=0
    max_so_far=0
    
    for i in range(0,n):
        
        max_ending_here=max_ending_here + arr[i]
       # print(max_ending_here)
        
        if max_ending_here < 0:
            max_ending_here=0
            
        elif (max_so_far < max_ending_here):
              max_so_far=max_ending_here
            
    return max_so_far
    
def kadanes_algo_efficient_neg_pos(arr,n):
    
    max_so_far=arr[0]
    max_ending_here=arr[0]
    
    for i in range(1,n):
        max_ending_here=max(arr[i],max_ending_here+arr[i])
        max_so_far=max(max_so_far,max_ending_here)
        
    return max_so_far
        
        
arr=[-2,-3, 4, -1, -2, 1, 5, -3]
print(arr)
n=len(arr)
ans=kadanes_algo_efficient_neg_pos(arr,n)
print(ans)