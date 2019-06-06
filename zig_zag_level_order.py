### Zig Zag Order traversal


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def zig_zag_level_order(root):
    if root is None:
        return
        
    currentlevel=[]
    nextlevel=[]
    
    ltr=True
    
    currentlevel.append(root)
    
    while(len(currentlevel) > 0):
        
        temp=currentlevel.pop(-1)
        print(temp.data)
        
        if ltr:
            if temp.left:
                nextlevel.append(temp.left)
            if temp.right:
                nextlevel.append(temp.right)
                
        else:
            if temp.right:
                nextlevel.append(temp.right)
            if temp.left:
                nextlevel.append(temp.left)
                
        if len(currentlevel)==0:
            
            ltr=not ltr
            
            currentlevel,nextlevel=nextlevel,currentlevel
            
            
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
print("Zigzag Order traversal of binary tree is") 
zig_zag_level_order(root) 