# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        import copy

        if root == None:
            return []

        # ret用来保存结果
        ret = []  # 用来最后return
        supportArrayList = [[root.val]]  # 用来保存路径
        support = [root]  # 用来做层序遍历

        while support:
            # 判断根节点
            tmpNode = support[0]
            tmpArrayList = supportArrayList[0]
            if tmpNode.left == None and tmpNode.right == None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)

            # 判断左节点
            if tmpNode.left:
                support.append(tmpNode.left)
                newTmpArrayList = copy.copy(tmpArrayList) #这里是浅拷贝
                newTmpArrayList.append(tmpNode.left.val)
                supportArrayList.append(newTmpArrayList)
            # 判断右节点
            if tmpNode.right:
                support.append(tmpNode.right)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.right.val)
                supportArrayList.append(newTmpArrayList)

            del support[0]
            del supportArrayList[0]

        return ret

if __name__ == '__main__':
    s = Solution()