# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #depth[u] = depth[previous] + 1
    def preOrder(self, u: Optional[TreeNode], depth: int):
        if u is None:
            return
        #Visit current node
        if len(self.answer) < depth + 1: #do phan tu bat dau tu next = 0
            self.answer.append(u.val)
        else:
            self.answer[depth] = max(self.answer[depth], u.val)
        # Go through left
        self.preOrder(u.left, depth + 1)
        # Go through right
        self.preOrder(u.right, depth + 1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.preOrder(root, 0)
        return self.answer
