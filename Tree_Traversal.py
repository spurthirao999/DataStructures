# Tree traversal
# Build tree from inorder,preorder

class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
        
        
def preorder(root):
    if(root):
        print(root.value)
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.value)
        inorder(root.right)
        
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.value)   
        

def build_tree(inorder,preorder,instrt,inend):
    if(instrt>inend):
        return None
        
    tnode = Node(preorder[build_tree.preIndex])
    build_tree.preIndex+=1
        
    index=inorder_dict[tnode.value]
    print("Index"+str(index)+tnode.value)
    
    tnode.left=build_tree(inorder,preorder,instrt,index-1)
    tnode.right=build_tree(inorder,preorder,index+1,inend)
    
    return tnode
    
def find_max_depth(root):
    if root is None:
        return
        
    else:
         return 1 +find_max_depth(root.left)
        
    
        
      
     
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
temp=root
print("Inorder traversal")
inorder(root)
print("Preorder Traversal")
preorder(temp)
print("Postorder Traversal")
PostOrder(temp)

build_tree.preIndex=0
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

#inOrder = ['D','B'] 
#preOrder = ['D','B']

inorder_dict=dict(zip(inOrder,range(len(inOrder))))
print(inorder_dict)
print(inorder_dict['D'])
root_new=build_tree(inOrder,preOrder,0,len(inOrder)-1)
print("Inorder traversal")
inorder(root_new)

x=find_max_depth(temp)
print(x)
