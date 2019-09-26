# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here

        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        a = 1  # 竖着覆盖
        b = 2  # 横着覆盖
        for i in range(3, number + 1):
            b = a + b # b = 原来a，b的和
            a = b - a # a = 原来的b

        return b

if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(10))