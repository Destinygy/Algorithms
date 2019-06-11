class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here

        ls = []
        if not root:
            return
        queue = [root]
        while len(queue) > 0:
            p = queue.pop(0)
            ls.append(p)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

        for i in range(len(ls)):
            q = ls[i]
            temp = q.left
            q.left = q.right
            q.right = temp
        return ls[0]

#构建二叉树
def create(ls):
    node=Node(ls[0])
    queue=[node]
    i=1
    while i < len(ls):
        par=queue.pop(0)
        par.left=Node(ls[i])
        queue.append(par.left)
        i += 1
        if i<len(ls):
            par.right=Node(ls[i])
            queue.append(par.right)
            i += 1
    return node

#层次遍历
def level(root):
    queue=[root]
    while queue:
        temp=queue.pop(0)
        print(temp.val)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

ls=[1,2,3,4,5,6]

mirror=Solution()
root=mirror.Mirror(create(ls))
level(root)
