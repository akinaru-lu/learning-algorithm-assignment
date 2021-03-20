# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def found(n):
            if not n:
                return False
            m = n == p or n == q
            l = found(n.left)
            r = found(n.right)
            
            if m + l + r >= 2:
                self.ans = n
            return m or l or r
        found(root)
        return self.ans
