# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        return pow(2,number - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(10))