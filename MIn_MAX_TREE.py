# Tree traversal
# Build tree from inorder,preorder

class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
        
        
#Find max and min elem in BT
def find_max_min(root):
    minimum =65635 
    
    if(root is not None):
        root_val=root.value
        left=find_max_min(root.left)
        right=find_max_min(root.right)
        if(left > right):
            minimum=right
            
        else:
            minimum=left
            
        if(root_val < minimum):
            minimum=root_val
        
            
    return minimum
    
#HEight of a tree or max dept og a tree
def height_of_a_tree(root):
    if(root is None):
        return 0
    else:
        left=height_of_a_tree(root.left)
        right=height_of_a_tree(root.right)
        
        height=max(left,right)
        return height + 1
        
#Find minimum depth of a binary tree
def minDepth(root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return minDepth(root.left)+minDepth(root.right)+1
        return min(minDepth(root.right),minDepth(root.left))+1
        
def find_deepest_node_in_a_tree(root,height):
    if(root is None):
        return None
    else:
        if(height==1):
            x=root.value
            return x
        else:
            find_deepest_node_in_a_tree(root.left,height - 1)
            find_deepest_node_in_a_tree(root.right,height - 1)
            
        
#Find leaves in a binary tree:
def find_leaves_BT(root):
    if root is None:
        return 0
        
    res=0
    if root.left is None and root.right is None:
            print(root.value)
            res+=1
            
    
    res+= find_leaves_BT(root.left) + find_leaves_BT(root.right)
    return res
    
             
#Find full nodes in a binary tree:
def find_full_nodes_BT(root):
    if root is None:
        return 0
        
    res=0
    if root.left and root.right:
            print(root.value)
            res+=1
            
    
    res+=find_full_nodes_BT(root.left) + find_full_nodes_BT(root.right)
         
    return res
    
                                 
count=0
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
#root.right.right.right=Node(8)
maximum=find_max_min(root)
#print(maximum)
height=height_of_a_tree(root)
print("Height"+str(height))
minDepth=minDepth(root)
#print(minDepth)
node_in_deepest_level=find_deepest_node_in_a_tree(root,height)
print(node_in_deepest_level)
print("Leaves")
count=find_leaves_BT(root)
print("COunt"+str(count))
fullnodes=find_full_nodes_BT(root)
print("Full Nodes"+str(fullnodes))
