# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if base == 1:
            return 1
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        else:
            return pow(base, exponent)

if __name__ == '__main__':
    s = Solution()
    print(s.Power(3,8))