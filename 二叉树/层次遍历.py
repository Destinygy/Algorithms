class Node(object):
    def __init__(self,val,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


def level(root):
    que=[root]
    res=[]
    while len(que):
        cur=que.pop(0)
        res.append(cur.val)
        if cur.left:
            que.append(cur.left)
        if cur.right:
            que.append(cur.right)
    for i in res:
        print(i,end=' ')
    return

tree=Node(1, Node(3, Node(7,Node(0)) , Node(6)), Node(2, Node(5), Node(4)))
level(tree)