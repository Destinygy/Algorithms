#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#扫描一遍数组，是奇数就放到指定（temp）位置
def reOrderArray(array):
    # write code here
    length = len(array)
    temp = 0
    for i in range(length):
        val = array[i]
        if val % 2 != 0:
            print(array.pop(i))
            array.insert(temp,val)
            temp += 1
    return array

 #前偶后奇就交换，类似冒泡法
def reOrderArray2(array):
    length=len(array)
    for i in range(length):
        for j in range(length-1,i,-1):
            if array[j] % 2 == 1 and array[j-1] % 2 == 0:
                array[j-1],array[j]=array[j],array[j-1]

    return array

input_ls=list(map(int,input().split(',')))
res=reOrderArray2(input_ls)
print(res)
