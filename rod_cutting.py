def rod_cutting_problem(price):
    
    price_new=[0]*(len(price)+1)
    print(price_new)
    
    price_new[0]=0
    for i in range(1,len(price)+1):
        max_val=-1
        for j in range(i):
            #print(price_new[i-j-1],i-j-1,i,j)
            max_val=max(max_val,price[j]+price_new[i-j-1])
        price_new[i]=max_val
    
    ans=0
    for i in range(1,len(price_new)):
        ans=max(ans,price_new[i])
        
    print(ans)
    
    
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
rod_cutting_problem(arr)