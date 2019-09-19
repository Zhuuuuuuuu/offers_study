# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.acceptstack = []
        self.outputstack = []

    def push(self, node):
        # write code here
        self.acceptstack.append(node)

    def pop(self):
        if self.outputstack == []:
            while self.acceptstack:
                self.outputstack.append(self.acceptstack.pop())

        if self.outputstack != []:
            return self.outputstack.pop()


if __name__ == '__main__':
    s = Solution()
    print(1,2,3,4,5)