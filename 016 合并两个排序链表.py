# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        newhead = pHead1 if pHead1.val < pHead2.val else pHead2

        p1 = pHead1
        p2 = pHead2
        preVious = newhead

        if newhead == p1:
            p1 = p1.next
        else:
            p2 = p2.next

        while p1 and p2:
            if p1.val < p2.val:
                preVious.next = p1
                preVious = p1
                p1 = p1.next
            else:
                preVious.next = p2
                preVious = p2
                p2 = p2.next

        if p1 == None:
            preVious.next = p2
        else:
            preVious.next = p1

        return newhead

if __name__ == '__main__':
    s = Solution()
    print(s.Merge([3,4,5,6],[1,3,6,9]))