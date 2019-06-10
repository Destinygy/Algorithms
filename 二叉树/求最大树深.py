class Node(object):
    def __init__(self,val,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

tree=Node(1, Node(3, Node(7,Node(0)) , Node(6)), Node(2, Node(5), Node(4)))

def deepth(root):
    if not root:
        return 0
    return  max(deepth(root.left),deepth(root.right)) + 1

print(deepth(tree))