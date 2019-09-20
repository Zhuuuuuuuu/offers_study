# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        # 创建两个栈分别以左序和右序进行输入结点
        stack1 = [pRoot]
        stack2 = []

        ret = []
        while stack1 or stack2:

            # 先左后右
            if stack1:
                tempret = []
                while stack1:
                    tempnode = stack1.pop()
                    tempret.append(tempnode.val)
                    if tempnode.left:
                        stack2.append(tempnode.left)
                    if tempnode.right:
                        stack2.append(tempnode.right)
                ret.append(tempret)

            # 先右后左
            if stack2:
                tempret = []
                while stack2:
                    tempnode = stack2.pop()
                    tempret.append(tempnode.val)
                    if tempnode.right:
                        stack1.append(tempnode.right)
                    if tempnode.left:
                        stack1.append(tempnode.left)
                ret.append(tempret)

        return ret
