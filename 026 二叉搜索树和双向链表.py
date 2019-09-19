# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None

        # 左子树一直向右找到最边上的结点
        def find_right(node):
            while node.right:
                node = node.right
            return node

        # 递归寻找左右结点
        leftnode = self.Convert(pRootOfTree.left)
        rightnode = self.Convert(pRootOfTree.right)

        retnode = leftnode #保存leftnode结点
        # 左子树找最右边的结点
        if leftnode:
            leftnode = find_right(leftnode)
        else:
            retnode = pRootOfTree #如果左子树不存在

        #将根节点做成双向链表
        pRootOfTree.left = leftnode
        pRootOfTree.right = rightnode
        if leftnode != None:
            leftnode.right = pRootOfTree
        if rightnode != None:
            rightnode.left = pRootOfTree

        return retnode
