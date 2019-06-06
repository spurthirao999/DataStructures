## Kth largest/smallest number
import heapq 

def findKthLargest4(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    print(heap)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    print(heap)
    return heapq.heappop(heap)
    
    
arr=[3,2,1,5,6,4]
num=2
x=findKthLargest4(arr,num)
print(x)