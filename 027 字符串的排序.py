# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join,itertools.permutations(ss)))))
    #set()是集合，作用是去除重复的数字
    #itertools.permutations()是求全排列
    #list的作用是为了sorted进行排序

if __name__ == '__main__':
    s = Solution()
    print(s.Permutation("abc"))