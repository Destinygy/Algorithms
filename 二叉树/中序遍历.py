def InOrder(ls):
    stack=[]
    res=[]
    i=0
    while i < len(ls) or len(stack) > 0:
        if i < len(ls):
            stack.append(ls[i])
            i = 2 * i + 1 #找左孩子
        else:
            p=stack.pop()
            res.append(p)
            ind=ls.index(p)
            i = 2 * ind + 2 #找右孩子
    for i in res:
        print(i , end=',')

if __name__ == '__main__':
    ls=[1,2,3,4,5,6,7,8,9,10]
    InOrder(ls)
