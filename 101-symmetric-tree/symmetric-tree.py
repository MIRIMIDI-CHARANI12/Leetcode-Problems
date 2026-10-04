# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def samet(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            lt=samet(p.left,q.right)
            rt=samet(p.right,q.left)
            if lt and rt:
                return True
            else:
                return False
        return samet(root.left,root.right)
            
        