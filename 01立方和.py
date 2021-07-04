# Author：DongXuewei
# Time  ：2021/7/4 16:47

"""
函数功能：判断某一非负整数能否写成两个整数的立方和。即，c = a^3 + b^3，若存在，返回是a和b中较大的那个；若不存在，返回-1。
测试用例：
输入：8
输出：2
"""
def cubeSumFunc():
    cubeSum = 91
    i=0
    j=0
    while i<=cubeSum:
        while i<=j<=cubeSum:
            if (i**3 + j**3 == cubeSum):
                #print(f"i={i},j={j}")
                return j
            else:
                j = j + 1
                if j > cubeSum:
                    j = i+1
                    break
        i=i+1
    else:
        # print(f"i={i},j={j}")
        return -1


print(cubeSumFunc())