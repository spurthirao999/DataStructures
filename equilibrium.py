def equilibrium(arr): 
  
    # finding the sum of whole array 
    total_sum = sum(arr) 
    leftsum = 0
    print(total_sum)
    for i, num in enumerate(arr): 
          
        # total_sum is now right sum 
        # for index i 
        print(num)
        total_sum -= num 
        print("TotalSum"+str(total_sum))
          
        if leftsum == total_sum: 
            print("EQUI"+str(i) )
        leftsum += num 
        print(leftsum)
       
      # If no equilibrium index found,  
      # then return -1 
    return -1
      
# Driver code 
arr = [-7, 1, 5, 2, -4, 3, 0] 
print ('First equilibrium index is ', 
       equilibrium(arr)) 