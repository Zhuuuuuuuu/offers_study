# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return None

        # 第一步：首先找到两个不一样的值
        twonumXor = None
        for num in array:
            if twonumXor == None:
                twonumXor = num
            else:
                twonumXor = twonumXor ^ num

        # 第二步：得到这两个数异或的结果，找到这两个数在第几位上异或的值为 1
        count = 0
        while twonumXor % 2 == 0:
            twonumXor = twonumXor >> 1  # 相当于除以二
            count += 1

        mask = 1 << count  # 相当于在1后面填上count个0

        # 第三步:通过mask可以将原数组分为两组，一组与mask与的结果为0,另一组与msk与的结果为1
        # 同时这两组中，每组包含了一个不相同的数
        firstnum = None
        secondnum = None

        for num in array:
            if num & mask == 0:
                if firstnum == None:
                    firstnum = num
                else:
                    firstnum = firstnum ^ num
            else:
                if secondnum == None:
                    secondnum = num
                else:
                    secondnum = secondnum ^ num

        return firstnum, secondnum


if __name__ == '__main__':
    s = Solution()
    print(s.FindNumsAppearOnce([4,3,4,3,2,1,1,6,7,7]))