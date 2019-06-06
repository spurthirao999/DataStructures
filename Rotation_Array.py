####################################
# This program contains code for:
# a) Left rotation of an array one by one for a given size ( O(n*d))
# b) Left rotation of an array in reversal manner (O(n))
# c) Both the ablove methods for Right Rotation as well
#  Example for Left & Right Rotation for arr={0,1,2,3,4,5} for size=2
# res={2,3,4,5,0,1} for Left
# res={4,5,0,1,2,3}for Right
#####################################################

def printArray(arr):
        for i in range(0,len(arr)):
             print("% d "%arr[i],end="")


def left_rotation(arr,size):
        for i in range(size):
            leftrotatebyOne(arr)
            
def leftrotatebyOne(arr):
    temp=arr[0]
    for i in range(0,len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr) - 1]=temp
    
    
def left_rotation_by_reversal(arr,k):
    n=len(arr)
    reverseArray(arr,0,k-1)
    reverseArray(arr,k,n-1)
    reverseArray(arr,0,n-1)
    
def reverseArray(arr,start,end):
    while(start < end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start += 1
        end -=1
        
def rightRotation(arr,size):
    
    for z in range(0,size):
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        
def rightRotationbyReversal(arr,k):
    n=len(arr)
    reverseArray(arr,n-k,n-1)
    reverseArray(arr,0,n-k-1)
    reverseArray(arr,0,n-1) 
    
def binarySearchproc(arr, l, r, key):
    
    if (r > 1):
        mid= (l + (r -1))//2
        
        if (key == arr[mid] ):
            return mid
            
        elif (key > arr[r]):
            return -1
            
        elif (key < arr[mid]):
            return binarySearchproc(arr,l,mid-1,key)
            
        elif(key > arr[mid]):
            return binarySearchproc(arr,mid+1,r,key)
            
          
    else:
        return -1
            
        
    
     

array = [1,2,3,4,5,6,7]
printArray(array)
print("\n After rotation")
left_rotation_by_reversal(array,2)
printArray(array)
array = [1,2,3,4,5,6,7]
print("\n Right Rotation")
rightRotationbyReversal(array,3)
#rightRotation(array,3)
printArray(array)
array = [1,2,3,4,5,6,7]
key=3
found=binarySearchproc(array,0,len(array)-1,key)
if found!=-1:
    print ("Elem found at position" + str(found ))
else:
    print("Elem not found")