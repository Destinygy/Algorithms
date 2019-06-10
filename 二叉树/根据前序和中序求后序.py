class Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def rebuild(pre,center):
    if not pre:
        return
    cur=Node(pre[0])
    index=center.index(pre[0])
    cur.left=rebuild(pre[1:index+1],center[:index])
    cur.right=rebuild(pre[index+1:],center[index+1:])
    return cur

def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print(root.val)

if __name__=="__main__":
    pre=list(map(int,input().split()))
    center=list(map(int,input().split()))
    res=rebuild(pre,center)
    deep(res)