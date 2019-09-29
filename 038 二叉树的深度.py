# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        else:
            left = self.TreeDepth(pRoot.left) + 1
            right = self.TreeDepth(pRoot.right) + 1
            depth = max(left, right)
            return depth

if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)

    l1.left = l2
    l2.left = l3
    l3.left = l4
    l1.right = l5
    l5.right = l6

    s = Solution()
    print(s.TreeDepth(l1))