class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
# 取出方式
# 1.深度优先
# 对于深度优先来说
# 1.先序遍历
# 2.中序遍历
# 3.后序遍历
# 注意：先序.中序.后序遍历都是对于根节点来说的，左右节点都是先左后右


# 2.广度优先

# # 前序遍历
# def preOrderRecusive(root):
#     if root == None:
#         return None
#     print(root.val)
#
#     preOrderRecusive(root.left)
#     preOrderRecusive(root.right)

# # 中序遍历
# def midOrderRecusive(root):
#     if root == None:
#         return None
#
#     midOrderRecusive(root.left)
#     print(root.val)
#     midOrderRecusive(root.right)

# 后续遍历
def lastOrderRecusive(root):
    if root == None:
        return None

    lastOrderRecusive(root.left)
    lastOrderRecusive(root.right)
    print(root.val)


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

    # preOrderRecusive(t1)
    # midOrderRecusive(t1)
    lastOrderRecusive(t1)
