#Left View of a Binary Tree

## DO a level order traversal : O(n)

## In case of Right View:
## he problem can also be solved using simple recursive traversal. We can keep track of level of 
##a node by passing a parameter to all recursive calls. The idea is to keep track of maximum level also. 
##And traverse the tree in a manner that right subtree is visited before left subtree. Whenever we see a node whose level 
##is more than maximum level so far, we print the node because this is the last node in its level

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def leftViewUtil(root,level,max_level):
        
        if root is None:
            return
            
        print("Level-Max",max_level,level)
        if max_level[0] < level:
            print("\t",root.data)
            max_level[0]=level
            
        leftViewUtil(root.left,level+1,max_level)
        leftViewUtil(root.right,level+1,max_level)
        
def leftView(root):
    max_level=[0]
    leftViewUtil(root,1,max_level)
    
root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 
  
leftView(root) 
        
            
        