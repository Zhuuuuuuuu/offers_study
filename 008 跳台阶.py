# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):

        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        result = 0
        a = 1
        b = 2

        for i in range(3, number + 1):
            result = a + b
            a = b
            b = result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(100))