
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res=0
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, root, res):
        if root:
            if not root.left and not root.right:
                self.res+= 10*res + root.val
            self.dfs(root.left,  10*res + root.val)
            self.dfs(root.right, 10*res + root.val)
            