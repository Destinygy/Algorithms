class Node(object):
    def __init__(self,val,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

tree1=Node(1, Node(3, Node(7,Node(0)) , Node(6)), Node(2, Node(5), Node(4)))
tree2=Node(1, Node(3, Node(7,Node(0)) , Node(6)), Node(2, Node(5), Node(4)))

def isSameTree(root1,root2):
    if root1 ==None and root2 == None:
        return True
    elif root1 and root2:
        return root1.val == root2.val and isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)
    else:
        return False

print(isSameTree(tree1,tree2))