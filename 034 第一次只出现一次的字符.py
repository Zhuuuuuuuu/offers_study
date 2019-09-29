# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i,element)

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        #用字典enumerate()来做
        if len(s) == 0:
            return -1
        for i,element in enumerate(s):
            if s.count(element) == 1:
                return i

if __name__ == '__main__':
    s = Solution()
    print(s.FirstNotRepeatingChar("aabbe"))