class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val==subRoot.val and self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)

if __name__ == "__main__":
    root=TreeNode(3)
    root.left=TreeNode(4)
    root.right=TreeNode(5)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(2)
    subRoot=TreeNode(4)
    subRoot.left=TreeNode(1)
    subRoot.right=TreeNode(2)
    s=Solution()
    print(s.isSubtree(root,subRoot))