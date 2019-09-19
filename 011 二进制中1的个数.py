# -*- coding:utf-8 -*-

# #C语言中六种位运算符：
# & 按位与
# | 按位或
# ^ 按位异或
# ~取反
# <<左移
# >>右移
class Solution:
    def NumberOf1(self, n):
        # write code here

        n = 0xFFFFFFFF & n

        """
        count = 0
        for c in str(bin(n)):
            if c == "1":
                count += 1
        return count

        """

        count = 0
        for i in range(32):
            mask = 1 << i
            if n & mask != 0:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(3))