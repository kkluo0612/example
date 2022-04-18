class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isValidBST(root):
    pre=float("-inf")
    if not root:
        return True
    if not isValidBST(root.left):
        return False
    if root.val<=pre:
        return False
    pre=root.val
    return isValidBST(root.right)


if __name__ == '__main__':
    root=TreeNode(2)
    root.left=TreeNode(1)
    root.right=TreeNode(3)
    print(isValidBST(root))