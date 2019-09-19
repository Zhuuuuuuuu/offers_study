# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        if pHead == None:
            return None

        # 第一步 是首先确定有没有环
        # 如果快指针为空，则说明没有环
        # 如果快指针等于慢指针，则说明有环存在

        fastpointer = pHead
        slowpointer = pHead

        while fastpointer and fastpointer.next:
            fastpointer = fastpointer.next.next
            slowpointer = slowpointer.next

            if slowpointer == fastpointer:
                break

        if fastpointer == None or fastpointer.next == None:
            return None

        # 第二步 让慢指针继续在环中走，快指针从头开始走
        # 这是两个指针的速度一样，若此时快指针等于慢指针，则说明找到了环入口

        fastpointer = pHead
        while fastpointer != slowpointer:
            fastpointer = fastpointer.next
            slowpointer = slowpointer.next

        print(fastpointer,slowpointer)

        return fastpointer

if __name__ == '__main__':
    n1 = ListNode(5)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(2)
    n5 = ListNode(1)
    n6 = ListNode(3)


    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n1

    s = Solution()
    pHead = s.EntryNodeOfLoop(n1)

    temp = pHead
    print(temp)
