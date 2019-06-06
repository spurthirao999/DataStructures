"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None: return 0
        if not root.children: return 1
        
            
        return max(self.maxDepth(child) for child in root.children) + 1
        