# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.minValue = []
        self.stack = []

    def push(self, node):
        self.stack.append(node)

        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)

    def pop(self):
        # write code here
        if self.stack == []:
            return None
        self.minValue.pop()
        return self.stack.pop()

    def top(self):
        # write code here
        if self.stack == []:
            return None
        return self.stack[-1]

    def min(self):
        # write code here
        if self.minValue == []:
            return None
        return self.minValue[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.min([2,3,4,5,1,12]))