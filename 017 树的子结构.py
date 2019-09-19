# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 判读为空的情况下
        if pRoot1 == None or pRoot2 == None:
            return False

        def hasEqual(pRoot1, pRoot2):
            if pRoot2 == None:
                return True
            if pRoot1 == None:
                return False
            # 判断根节点
            if pRoot1.val == pRoot2.val:
                if pRoot2.left == None:
                    leftEqual = True
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left)
                if pRoot2.right == None:
                    rightEqual = True
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right)
                return leftEqual and rightEqual
            return False

        # 判断根节点是否相同
        if pRoot1.val == pRoot2.val:
            result = hasEqual(pRoot1, pRoot2)
            if result:
                return True

        # 判断左节点是否相同
        result = self.HasSubtree(pRoot1.left, pRoot2)
        if result:
            return True
        # 判断右节点是否相同
        result = self.HasSubtree(pRoot1.right, pRoot2)

        return result


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left = t2
    t1.right= t3
    t2.left = t4
    t2.right= t5
    t3.left = t6
    t3.right= t7
    t6.right= t8


    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)

    l1.left = l2
    l1.right = l3
    l2.right = l4


    s = Solution()
    print(s.HasSubtree(t1,l1))