#Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. 
#And the rightmost element is always a leader. 
#For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2. 
def leaders_arr(arr):
    n=len(arr)
    
    max_from_right=arr[n-1]
    print(max_from_right)
    
    for i in range(n-2,0,-1):
        if arr[i] > max_from_right:
            max_from_right=arr[i]
            print(max_from_right)
        
    
    
arr = [16, 17, 4, 3, 5, 2] 
leaders_arr(arr)