# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead

        left = pHead
        mid = pHead.next
        right = mid.next

        left.next = None

        while right != None:
            mid.next = left
            left = mid
            mid = right
            right = right.next

        mid.next = left
        return mid