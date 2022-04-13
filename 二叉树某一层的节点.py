class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def TransLevel(root,level):
    if not root:
        return
    else:
        if level==1 and isinstance(root,TreeNode):
            print(root.val)
        else:
            if isinstance(root,TreeNode):
                TransLevel(root.left,level-1)
                TransLevel(root.right,level-1)

root = TreeNode(9)
root.left=TreeNode(7)
root.right=TreeNode(8)
root.left.left=TreeNode(6)
root.right.right=TreeNode(5)
root.left.left.left=TreeNode(2)
root.right.right.right=TreeNode(1)
TransLevel(root,3)