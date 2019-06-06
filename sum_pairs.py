def find_sum_pairs_hashing(arr,sum):
    s=set()
    found = 1
    count=0
    
    for i in range(0,len(arr)-1):
        temp=sum-arr[i]
        if(temp in s and temp>=0):
            count+=1
            print("The pair is found for the sum "+str(sum)+" and is \n("+str(arr[i])+","+str(temp)+")"+str(count))
            found = 0
            
        s.add(arr[i])
        
    if(found == 1):
        print("Pair not found")
        
# This function returns True  
# if arr[0..n-1] has a pair 
# with sum equals to x. 
def pairInSortedRotated( arr, n, x ): 
      
    # Find the pivot element 
    for i in range(0, n - 1): 
        if (arr[i] > arr[i + 1]): 
            break; 
              
    # l is now index of smallest element         
    l = (i + 1) % n 
    # r is now index of largest element 
    r = i      
  
    # Keep moving either l  
    # or r till they meet 
    print(str(l))
    print(str(r))
    while (l !=r): 
          
        # If we find a pair with  
        # sum x, we return True 
        if (arr[l] + arr[r] == x): 
            return True; 
              
        # If current pair sum is less, 
        # move to the higher sum 
        if (arr[l] + arr[r] < x): 
            l = (l + 1) % n; 
        else: 
              
            # Move to the lower sum side 
            r = (n + r - 1) % n; 
      
    return False;             
            
    
    
           
            
        
    
        
        
A = [1,4,45,6,10,8,3,2] 
n = 5
find_sum_pairs_hashing(A,n)
arr = [11, 15, 26, 38, 9, 10] 
sum1 = 19
n = len(arr) 
  
if (pairInSortedRotated(arr, sum1,n)): 
    print ("Array has two elements with sum 19") 
else: 
    print ("Array doesn't have two elements with sum 19 ") 