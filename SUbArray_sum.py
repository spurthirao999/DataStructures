def find_sum_subarray(arr,n,sum):
    curr_sum = arr[0]
    i = 1
    start=0
    
    while(i < n):
        
        while(curr_sum > sum and start < i -1):
            curr_sum=curr_sum - arr[start]
            start+=1
            
        if curr_sum == sum:
            print("SUm found between indices")
            print("%d and %d"%(start,i-1))
            return 1
            
        if i<n:
            curr_sum=curr_sum + arr[i]
            
        i+=1
        
    print("No subarray found")
    return 0
    
def find_subArray_neg(arr,n,k):
    
    Map={}
    
    curr_sum=0
    
    for i in range(0,n):
        curr_sum=curr_sum + arr[i]
        
        
        # if curr_sum is equal to target sum  
        # we found a subarray starting from index 0  
        # and ending at index i
        if(curr_sum == k):
            print("Sum found be/w indices 0 to",i)
            return
            
        if(curr_sum - sum) in Map:
            print("Sum found b/w indices ",Map[curr_sum - sum]+1, "to",i)
            return
            
        Map[curr_sum] = i
        
    print("No subarray")
    
arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 14

arr1 = [10, 2, -2, -20, 10]  
n1 = len(arr)  
sum1=-10
 
find_sum_subarray(arr, n, sum)
find_subArray_neg(arr1,n1,sum1)