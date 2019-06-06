## Breadth First search
from collections import defaultdict
#import queue


class Graph:
    
    def __init__(self):
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def print_graph(self):
        for i in self.graph:
            print(i)
            
    def BFS(self,vertex):
        queue=[]
        visited={}
        
        for i in self.graph:
            visited[i]=False
            
        queue.append(vertex)
        visited[vertex]=True
        
        while queue:
            s=queue.pop(0)
            print(s)
            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True
                    
            
        
        
            
        
        
        
        
            
            
            
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
#g.print_graph()
g.BFS("A")