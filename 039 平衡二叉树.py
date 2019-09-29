# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def DepthTree(self, pRoot):
        if not pRoot:
            return 0
        return max(self.DepthTree(pRoot.left) + 1, self.DepthTree(pRoot.right) + 1)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left, right = 0, 0
        left = self.DepthTree(pRoot.left)
        right = self.DepthTree(pRoot.right)
        if abs(left - right) == 1 or left - right == 0:
            return True
        else:
            return False

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
    print(s.IsBalanced_Solution(l1))