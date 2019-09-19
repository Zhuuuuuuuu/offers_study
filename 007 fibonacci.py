# -*- coding:utf-8 -*-
class Solution:
    '''
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            num = self.Fibonacci(n-1)+self.Fibonacci(n-2)
            return num
        return None
        '''

    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        a = 1
        b = 0
        result = 0
        for i in range(0, n - 1):
            result = a + b
            b = a
            a = result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(100))