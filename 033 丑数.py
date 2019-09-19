# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here

        if index < 1:
            return 0

        uglyList = [1]
        uglycount = 1
        twopointer = 0
        threepointer = 0
        fivepointer = 0

        while uglycount != index:
            minvalue = min(2 * uglyList[twopointer], 3 * uglyList[threepointer], 5 * uglyList[fivepointer])
            uglycount += 1 #每找到一个丑数，uglycount加一
            uglyList.append(minvalue)

            if 2 * uglyList[twopointer] == minvalue:
                twopointer += 1
            if 3 * uglyList[threepointer] == minvalue:
                threepointer += 1
            if 5 * uglyList[fivepointer] == minvalue:
                fivepointer += 1

        return uglyList[uglycount - 1]

if __name__ == '__main__':
    s = Solution()
    result = s.GetUglyNumber_Solution(5000000)
    print(result)