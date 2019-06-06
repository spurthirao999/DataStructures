### FInd the missing number

def find_missing_number(arr):
    n=len(arr)
    x2=1
    
    x1=arr[0]
    for i in range(1,n):
        x1 = x1 ^ arr[i]
        
    for i in range(2,n+2):
        x2=x2 ^ i
    
    return x1 ^ x2
    
    
arr=[1, 2, 4,6, 3, 7, 8]
n=find_missing_number(arr)
print(n)