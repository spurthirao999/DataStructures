# -*- coding: utf-8 -*-
### Active and inactive cells in an array after k days

## Given a binary array of size n where n > 3. A true (or 1) value in the array means active and false (or 0) means inactive.
#Given a number k, the task is to find count 
#of active and inactive cells after k days. After every day, status of i’th cell becomes 
#active if left and right cells are not same and inactive if left and right cell are same (both 0 or both 1).
#Since there are no cells before leftmost and after rightmost cells, the value cells before leftmost 
#and after rightmost cells is always considered as 0 (or inactive).

def compute_active_inactive_cells(arr,days):
    
    n=len(arr)
    temp=[False]*(n)
    
    for i in range(0,n):
        temp[i]=arr[i]
        
    print(temp)
    
    while(days > 0):
        temp[0]=False ^ arr[1]
        temp[n-1]=False^arr[n-2]
        
        for i in range(1,n-2+1):
            temp[i]=arr[i-1] ^ arr[i+1]
            
        for i in range(n):
            arr[i]=temp[i]
            
        days-=1
    
    print(arr)
    
    
arr=[0, 1, 0, 1, 0, 1, 0, 1]
k=3
compute_active_inactive_cells(arr,k)