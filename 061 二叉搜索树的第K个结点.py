#本题采用中序列遍历--》刚刚后就是从小到大第k个节点

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here

        retList = []

        def preOrder(pRoot):
            if pRoot == None:
                return None

            preOrder(pRoot.left)
            retList.append(pRoot)
            preOrder(pRoot.right)

        preOrder(pRoot)

        if len(retList) < k or k < 1:
            return None

        return retList[k - 1]