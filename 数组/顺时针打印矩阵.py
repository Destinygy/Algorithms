class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        if n==1 and m==1:
            return [matrix[0][0]]

        for o in range( (min(n,m) + 1) // 2 ):
            [res.append(matrix[o][i]) for i in range(o,m-o)]
            [res.append(matrix[j][m-1-o]) for j in range(o+1,n-o)]
            [res.append(matrix[n-1-o][k]) for k in range(m-1-o-1,o-1,-1)]
            [res.append(matrix[l][o]) for l in range(n-1-o-1,o,-1)]

        for i in res:
            print(i,end=" ")

solution=Solution()
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
solution.printMatrix(matrix)