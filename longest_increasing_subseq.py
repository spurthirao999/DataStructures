## Longest increasing SUbsequence

## LS[i]=1 + max(LS(j)) where j<i and A[i]>A[j]

## [10,22,9,33,21,50,41,60,80]

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def longestIncreasingSubsequence(arr):
    
    
    n=len(arr)
    lis=[1] * n
    
    if n==1:
        return 1
    x=[]
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] :
                    lis[i]=max(lis[i],lis[j]+1)
                    #print(lis[i],arr[i])
                 
                
    print(x)
                   
                    


    print(lis)

    ans=0  
    for i in range(1,n):
        ans=max(ans,lis[i])

    return ans


if __name__ == '__main__':
    

    arr = [10,22,9,33,21,50,41,60,80]


    result = longestIncreasingSubsequence(arr)

    print(result)

    