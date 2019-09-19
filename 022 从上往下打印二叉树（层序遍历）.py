# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here

        # 规律： 1.每次打印一个节点的时候，如果该节点有子节点，则把该节点的子节点放到一个队列的末尾。
        #       2.接下来到队列的头部去除最早进入队列的节点，重复之前的打印操作，知道队列所有的节点都被打印出来
        if root == None:
            return []

        support = [root]
        ret = []
        while support:
            tempnode = support[0]
            ret.append(tempnode.val)

            if tempnode.left:
                support.append(tempnode.left)
            if tempnode.right:
                support.append(tempnode.right)

            del support[0]
        return ret