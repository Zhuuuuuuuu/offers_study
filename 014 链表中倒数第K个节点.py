# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        first = head
        second = head

        for i in range(k):
            if first == None:
                return None
            first = first.next

        while first != None:
            first = first.next
            second = second.next

        return second

if __name__ == '__main__':
    s = Solution()
    print(s.FindKthToTail(0,5))