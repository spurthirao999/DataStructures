#Minimum number of platforms
#O(nlogn)

def min_number_of_platforms(arr,dep,n):
    arr.sort()
    dep.sort()
    
    
    no_of_platforms=1
    result=1
    i=1
    j=0
    
    while(i<n and j<n):
        
        if arr[i] < dep[j]:
            no_of_platforms+=1
            i+=1
                
            if result < no_of_platforms :
                print(arr[i])
                result=no_of_platforms
            
        else:
            no_of_platforms-=1
            j+=1
            
    return result
    
    
    
    
    
    
    
    
    
    
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
result=min_number_of_platforms(arr,dep,n)
print(result)