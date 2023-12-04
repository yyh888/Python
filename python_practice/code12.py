class TreeNode:
    a = 120
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

x = TreeNode
x.val = 100
print(x.a)