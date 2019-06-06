#Reverse an array in groups of given size.

def reverse_array_in_groups(arr,n,k):
    
    i=0
    while i < n:
        
        left =i
        right=min(i+k-1,n-1)
        
        while(left < right):
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right-=1
            
        i+=k
        
arr=[1,2,3,4,5,6,7,8]
print("Original Array \n"+str(arr))
n=len(arr)
k=3
reverse_array_in_groups(arr,n,k)
print("Reversed array in groups \n"+str(arr))