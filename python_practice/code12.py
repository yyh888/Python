class Solution(object):
    ret = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.bstToGst(root.right)
        self.ret += root.val
        root.val = self.ret
        self.bstToGst(root.left)
        return root
