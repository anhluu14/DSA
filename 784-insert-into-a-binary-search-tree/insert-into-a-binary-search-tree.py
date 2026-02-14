# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            new_node = TreeNode(val)
            return new_node #cay co 1 not
            
        if root.val > val:
            if root.left is not None:
                self.insertIntoBST(root.left, val)
                return root
            else:
                new_node = TreeNode(val)
                root.left = new_node
                return root
        if root.val < val:
            if root.right is not None:
                self.insertIntoBST(root.right, val)
                return root
            else:
                new_node =TreeNode(val) #tao nut moi
                root.right = new_node
                return root
