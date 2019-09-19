# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#在知道中序遍历和前序遍历的前提下,把二叉树给重建出来

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        if len(pre) != len(tin):
            return None

        # 第一步：取出pre的值,记录根节点在中序遍历的位置

        root = pre[0]  # 取出根节点的数值
        rootnode = TreeNode(root)  # 构造根节点

        pos = tin.index(root)

        # 第二步：找出左右子树
        tinleft = tin[:pos]
        tinright = tin[pos + 1:]

        preleft = pre[1:pos+1]
        preright = pre[pos + 1:]

        leftnode = self.reConstructBinaryTree(preleft, tinleft)
        rightnode = self.reConstructBinaryTree(preright, tinright)

        if leftnode:
            rootnode.left = leftnode
        if rightnode:
            rootnode.right = rightnode

        return rootnode


if __name__ == '__main__':
    s = Solution()
    result = s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    print(TreeNode)
