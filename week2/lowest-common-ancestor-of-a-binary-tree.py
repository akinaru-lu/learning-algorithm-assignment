# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'Treeroot', p: 'Treeroot', q: 'Treeroot') -> 'Treeroot':
        def found(node):
            if not node:
                return False
            left = found(node.left)
            right = found(node.right)
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        found(root)
        return self.ans
