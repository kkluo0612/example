class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right =None

def maxPathSum(root):
    if not root:
        return 0
    maxSum=root.val
    def dfs(node,maxSum):
        if not node:
            return 0
        left=max(0,dfs(node.left))
        right=max(0,dfs(node.right))
        maxSum=max(maxSum,left+right+node.val)
        return node.val+max(left,right)
    dfs(root,maxSum)
    return maxSum

if __name__ == "__main__":
    root=TreeNode(-10)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(7)
    print(maxPathSum(root))