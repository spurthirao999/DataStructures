## Depth First Search
## Count the number of islands


from collections import defaultdict
import numpy

class Graph:
    def __init__(self): 
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def dfs(self,key):
        
        visited={}
        print("Key",key)
        
        for key1 in self.graph:
            visited[key1] = False
            
        self.dfsUtil(key,visited)
                     
    def dfsUtil(self,key,visited):
        
        #print("Entered",key)
        visited[key] = True
        print(key)
        
        for i in self.graph[key]:
           # print(i,key)
            #print(visited[i])
            if visited[i] == False:
                self.dfsUtil(i,visited)
                
    def numIslands(self, grid):
        
        print(grid)
        if not grid:
            return 0
        n=len(grid)
        print(n)
        m=len(grid[0])
        print(m)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs_island(grid, i, j)
                    count += 1
        return count               
                        
    def dfs_island(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = '#'    
        self.dfs_island(grid, i+1, j)
        self.dfs_island(grid, i-1, j)
        self.dfs_island(grid, i, j+1)
        self.dfs_island(grid, i, j-1)
                   
        
    def print_key(self):
        for i in self.graph:
            print(i)   
            
            
g=Graph()
g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("A","G")
g.addEdge("A","E")
g.addEdge("B","A")
g.addEdge("C","D")
g.addEdge("C","A")
g.addEdge("D","C")
g.addEdge("D","F")
g.addEdge("E","A")
g.addEdge("F","D")
g.addEdge("G","A")
#g.dfs("A") 

rows,cols=(5,5)

arr=numpy.array([0] * 25).reshape((5,5))

arr = [[1, 1, 0, 0, 1], 
        [1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 1, 1, 0, 0], 
        [1, 1, 0, 1, 1]]
        
arr1=[[1],[1]]
            
n=g.numIslands(arr1)
print(n)

            


        
        
    
        
