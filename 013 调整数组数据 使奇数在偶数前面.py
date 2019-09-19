# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        ret = []

        for i in array:
            if i % 2 == 1:
                ret.append(i)

        for i in array:
            if i % 2 == 0:
                ret.append(i)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray([1,3,4,6,7,5,9]))