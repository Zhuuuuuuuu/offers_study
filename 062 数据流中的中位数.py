# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()

    def GetMedian(self,data):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0
        else:
            return self.data[int(length // 2)]

if __name__ == '__main__':
    s = Solution()
    print(s.GetMedian([1,2,3,4,5,6,7,8,9,10]))