def PostOrder(ls):
    stack=[]
    res=[]
    i=0
    lastvisit=-1
    while i < len(ls):
        stack.append(ls[i])
        i = 2 * i + 1
    while len(stack) > 0:
        p=stack.pop()
        ind=ls.index(p)
        right=2 * ind + 2
        if right >= len(ls) or lastvisit == right: #如果没有右子树或者右子树已经被访问过，则直接输出根节点
            res.append(p)
            lastvisit=ind
        else:                                      #否则进入右子树遍历
            stack.append(p)
            i=2 * ind + 2
            while i < len(ls):
                stack.append(ls[i])
                i = 2 * i + 1
    for i in res:
        print(i ,end=',')

if __name__ == '__main__':
    ls=[1,2,3,4,5,6,7,8,9,10]
    PostOrder(ls)