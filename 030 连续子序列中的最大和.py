# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):

        maxnum = None
        tempnum = 0

        for i in array:
            if maxnum == None:
                maxnum = i
            if tempnum + i < i:
                tempnum = i
            else:
                tempnum += i

            if maxnum < tempnum:
                maxnum = tempnum
        return maxnum


if __name__ == '__main__':
    s = Solution()
    print(s.FindGreatestSumOfSubArray([2,3,5,-18,3,4,6,2,-8]))