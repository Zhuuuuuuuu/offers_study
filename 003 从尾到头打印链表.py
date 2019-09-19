# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        ptmp = listNode

        while ptmp:
            result.insert(0, ptmp.val)
            ptmp = ptmp.next

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.printListFromTailToHead([2,3,4,5]))