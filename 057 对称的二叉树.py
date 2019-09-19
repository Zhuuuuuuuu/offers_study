# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # 定义判断是否对称的函数
        def isMirror(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            ret1 = isMirror(left.left, right.right)
            ret2 = isMirror(left.right, right.left)

            return ret1 and ret2

            # 如果根节点为空

        if pRoot == None:
            return True

        return isMirror(pRoot.left, pRoot.right)

if __name__ == '__main__':
    s = Solution()

    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(2)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(5)
    l7 = TreeNode(4)



    l1.right = l2
    l1.left = l3

    l2.left = l4
    l2.right = l5

    l3.right = l7
    l3.left = l6

print(s.isSymmetrical(l1))