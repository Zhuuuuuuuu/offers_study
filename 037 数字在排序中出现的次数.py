# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1,3,4,5,5,5,5],5))