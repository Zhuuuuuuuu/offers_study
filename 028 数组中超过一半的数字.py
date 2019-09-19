# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 以下方法时间复杂度为o(n),空间复杂度为o(1)
        last = 0
        lastcount = 0

        for num in numbers:
            # 前后不一样怼掉
            if lastcount == 0:
                last = num
                lastcount = 1
            # 前后一样的话
            else:
                if last == num:
                    lastcount += 1
                # 后面一个与前面不一样的话
                else:
                    lastcount -= 1

        # 剩下那个数可能是超过一半的数字
        if lastcount == 0:
            return 0
        else:
            lastcount = 0
            for num in numbers:
                if last == num:
                    lastcount += 1
            if lastcount > (len(numbers)) // 2:
                return last

        return 0

        # 以下方法时间复杂度为o(n),空间复杂度为o(n)
        # """
        # numscount = {}
        # length = len(numbers)
        #
        # for num in numbers:
        #     if num in numscount:
        #         numscount[num] += 1
        #     else:
        #         numscount[num] = 1
        #
        #     if numscount[num] > length//2:
        #         return num
        #
        # return 0
        # """

if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([5,5,5,5,5,5,5,5,3,2,1,3]))