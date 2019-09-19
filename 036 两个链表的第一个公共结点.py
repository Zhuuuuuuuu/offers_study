# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, head1, head2):
        # write code here
        list1 = []
        list2 = []
        node1 = head1
        node2 = head2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next


    # def FindFirstCommonNode(self, pHead1, pHead2):
    #     # write code here
    #     p1 = pHead1
    #     p2 = pHead2
    #
    #     while p1 and p2:
    #         p1 = p1.next
    #         p2 = p2.next
    #
    #     if p1:
    #         k = 0
    #         #寻找链表长度之间的差值
    #         while p1:
    #             p1 = p1.next
    #             k +=1
    #
    #         p1 = pHead1
    #         #先让长的那个走K步
    #         for i in range(k):
    #             p1 = p1.next
    #
    #
    #         while p1 != p2:
    #             p1 = p1.next
    #             p2 = p2.next
    #
    #         return p2
    #     if p2:
    #         k = 0
    #         # 寻找链表长度之间的差值
    #         while p2:
    #             p2 = p2.next
    #             k += 1
    #
    #         p2 = pHead2
    #         # 先让长的那个走K步
    #         for i in range(k):
    #             p2 = p2.next
    #
    #         while p1 != p2:
    #             p1 = p1.next
    #             p2 = p2.next
    #
    #         return p1

if __name__ == '__main__':
    s = Solution()

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    t1 = ListNode(2)
    t2 = ListNode(3)
    t3 = ListNode(5)
    t4 = ListNode(6)
    t5 = ListNode(7)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

print(s.FindFirstCommonNode(l1,t1))
