# -*- coding:utf-8 -*-

# 通项规律： f(n) = (f(n-1)+m) % n
#          1. f(n)是最终找到的那个值
#          2. % n的作用是防止超过最大长度 例如n=11 m=5 那么（10+5）%11 = 5
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here

        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i

        return last


if __name__ == '__main__':
    s = Solution()
    print(s.LastRemaining_Solution(10,3))