
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowwestCommonAncestor(self,root,nodes):
        nodes=set(nodes)
        size=len(nodes)

        ans=None
        def dfs(node):
            if not node:
                return 0
            v=dfs(node.left)+dfs(node.right)+(1 if node in nodes else 0)
            if v==size:
                nonlocal ans
                if ans is None:
                    ans=node
            return v
        dfs(root)
        print(ans)

if __name__ == "__main__":
    root=TreeNode(3)
    root.left=TreeNode(5)
    root.right=TreeNode(1)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.right.left=TreeNode(0)
    root.right.right=TreeNode(8)
    root.left.left.left=TreeNode(7)
    root.left.left.right=TreeNode(4)
    nodes=[4,7]
    s=Solution()
    s.lowwestCommonAncestor(root,nodes)