class TreeNode:
    def __init__(self, data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

root=TreeNode(1)
root.leftnode=TreeNode(2)
root.leftnode.leftnode=TreeNode(3)
root.leftnode.rightnode=TreeNode(4)
root.rightnode=TreeNode(5)
root.rightnode.leftnode=TreeNode(6)
root.rightnode.rightnode=TreeNode(7)

def inorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    print(root.data)
    if root.rightnode!=None:
        inorder(root.rightnode)

def preorder(root):
    print(root.data)
    if root.leftnode!=None:
        preorder(root.leftnode)
    if root.rightnode!=None:
        preorder(root.rightnode)

def postorder(root):
    if root.leftnode!=None:
        postorder(root.leftnode)
    if root.rightnode!=None:
        postorder(root.rightnode)
    print(root.data)

postorder(root)