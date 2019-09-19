# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None

        # 处理根节点
        root.right, root.left = root.left, root.right

        # 处理左子树
        # 处理右子树

        self.Mirror(root.left)
        self.Mirror(root.right)

if __name__ == '__main__':
    s = Solution()
    print(s.Mirror({5,4,3,2,1,8}))