# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
import copy

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        '''
        ret = copy.deepcopy(pHead)
        return ret
        '''

        if pHead == None:
            return None
        # 第一步：对每个节点生成一个一模一样的节点
        temp = pHead
        while temp:
            node = RandomListNode(temp.label)
            node.next = temp.next
            temp.next = node
            temp = node.next

        # 第二步：复制random指向
        temp = pHead
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # 第三步：拆开链表 断开链表之间的链接
        temp = pHead #第一个节点
        newtemp = pHead.next #第一个节点的后一个节点
        newHead = pHead.next #不变的头指针，作为返回值

        while temp:
            temp.next = temp.next.next
            if newtemp.next:
                newtemp.next = newtemp.next.next
                newtemp = newtemp.next
            temp = temp.next

        return newHead


if __name__ == '__main__':
     n1 = RandomListNode(1)
     n2 = RandomListNode(2)
     n3 = RandomListNode(3)
     n4 = RandomListNode(4)
     n5 = RandomListNode(5)
     n6 = RandomListNode(6)

     n1.next = n2
     n2.next = n3
     n3.next = n4
     n4.next = n5

     s = Solution()
     newhead = s.Clone(n1)

     tmp = newhead
     while tmp:
         print(tmp.label)
         tmp = tmp.next

