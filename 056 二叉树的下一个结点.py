# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            tempnode = pNode.right
            while tempnode.left:
                tempnode = tempnode.left
            return tempnode

        else:
            tempnode = pNode
            while tempnode.next:
                if tempnode.next.left == tempnode:
                    return tempnode.next
                tempnode = tempnode.next
            return None